import serial
import threading
import logging
from queue import Queue


class SerialThread(threading.Thread):
    """
    Class for concurrent processing of serial data
    """
    MODE_READ = 0
    MODE_WRITE = 1
    ACK = bytes.fromhex('23')

    def __init__(self, port=None):
        super().__init__(name='serial-thread')
        self.logger = logging.getLogger(self.name)
        self.requests = Queue()
        self.responses = Queue()
        self.__stop_event = threading.Event()
        self.__mode = self.MODE_WRITE
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

    def stop(self):
        self.__stop_event.set()

    def set_read(self):
        self.__mode = self.MODE_READ

    def set_write(self):
        self.__mode = self.MODE_WRITE

    def run(self):
        # Handshake with 0x23, stop thread if not responding
        connected = False
        try:
            self.serial_port.write(self.ACK)
            if self.serial_port.read(1) == self.ACK:
                connected = True
        except serial.SerialTimeoutException:
            self.logger.error('Failed to connect')
        if connected:
            # Main loop
            while not self.__stop_event.is_set():
                if self.__mode == self.MODE_WRITE and not self.requests.empty():
                    pass
                elif self.__mode == self.MODE_READ and self.serial_port.in_waiting > 0:
                    pass
