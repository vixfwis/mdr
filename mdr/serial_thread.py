import serial
import threading


class SerialThread(threading.Thread):
    """
    Class for concurrent processing of serial data
    """
    def __init__(self, port=None):
        super().__init__(name='serial-thread')
        self.__stop_event = threading.Event()
        self.serial_port = serial.serial_for_url(
            port,
            baudrate=19200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=None,
            xonxoff=False,
            write_timeout=5,
        )

    def stop(self):
        self.__stop_event.set()

    def run(self):
        while not self.__stop_event.is_set():
            pass
