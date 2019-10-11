# -*- coding: utf-8 -*-

import serial
import threading
import logging
from queue import Queue
from mdr.messages import ResponseFactory
from time import time, sleep

from mdr.utils.port import find_port


class SerialThread(threading.Thread):
    """
    Class for concurrent processing of serial data
    """
    MODE_READ = 0
    MODE_WRITE = 1
    ACK = bytes.fromhex('23')
    ABORT = bytes.fromhex('89')

    def __init__(self, port=None):
        super().__init__(name='serial-thread')
        self.logger = logging.getLogger(self.__class__.__name__)
        self.requests = Queue()
        self.response_factory = ResponseFactory()
        self.connected = False
        self.status_func = None
        self.__stop_event = threading.Event()
        self.__abort_event = threading.Event()
        self.__mode = self.MODE_WRITE
        self.__message = None
        if port is None:
            port = find_port()
        self.serial_port = serial.serial_for_url(
            port,
            baudrate=19200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=5,
            xonxoff=False,
            write_timeout=5,
        )

    def setStatusFunc(self, func):
        self.status_func = func

    def set_status(self, status):
        if self.status_func is not None:
            self.status_func(status)

    def stop(self):
        self.__stop_event.set()

    def abort_current_task(self):
        self.__abort_event.set()

    def set_read(self):
        self.__mode = self.MODE_READ

    def set_write(self):
        self.__mode = self.MODE_WRITE

    def get_mode(self):
        return self.__mode

    def get_blocking_event(self):
        return self.response_factory.blocking_event

    def unblock(self):
        self.response_factory.continue_event.set()

    def run(self):
        # Handshake with 0x23, stop thread if not responding
        self.logger.debug('Starting serial thread')
        self.set_status('Подключение...')
        try:
            self.serial_port.write(self.ACK)
            if self.serial_port.read(1) == self.ACK:
                self.connected = True
                self.set_status('Подключено')
        except serial.SerialTimeoutException:  # pragma: no cover
            self.logger.error('Failed to connect')
            self.set_status('Ошибка подключения')
        if self.connected:
            # Main loop
            while not self.__stop_event.is_set():
                sleep(0.01)
                self.set_status('Ожидание')
                if self.__abort_event.is_set():
                    self.serial_port.write(bytes.fromhex('89'))
                    self.serial_port.read(1)
                    self.set_write()
                    self.response_factory.reset()
                    self.__abort_event.clear()
                if self.__mode == self.MODE_WRITE and not self.requests.empty():
                    self.set_status('Передача')
                    self.__message = self.requests.get()
                    self.logger.debug('Received message from request queue: {}'.format(self.__message))
                    for byte in self.__message.get_bytes():
                        sleep(0.01)
                        self.logger.debug('Sending 0x{}'.format(bytes([byte]).hex()))
                        self.serial_port.write(bytes([byte]))
                        self.logger.debug('Waiting for ACK byte response')
                        if self.serial_port.read(1) == self.ACK:
                            self.logger.debug('ACK received')
                            self.__message.inc_sent_count()
                    if self.__message.expect_response() is not None:
                        self.logger.debug('Message is expecting response, switching to read mode')
                        self.set_read()
                elif self.__mode == self.MODE_READ and self.serial_port.in_waiting > 0:
                    t = time()
                    while time() - t < self.__message.get_delay():
                        sleep(0.01)
                        if self.__abort_event.is_set():
                            self.serial_port.write(bytes.fromhex('89'))
                            self.serial_port.read(1)
                            self.set_write()
                            self.response_factory.reset()
                            self.__abort_event.clear()
                            break
                        self.set_status('Прием')
                        if not self.response_factory.chk_fin(self.__message.expect_response()):
                            t = time()
                        if self.serial_port.in_waiting > 0:
                            t = time()
                            b = self.serial_port.read(1)[0]
                            self.logger.debug('Received 0x{}'.format(bytes([b]).hex()))
                            self.response_factory.submit(b)
                            self.logger.debug('Writing ACK to serial port')
                            self.serial_port.write(self.ACK)
                            self.__message.inc_rcv_count()
                    self.logger.debug('Switching back to write mode')
                    self.set_write()
        else:
            raise serial.SerialException('Could not connect')  # pragma: no cover
