from sys import stderr
from time import sleep

from mdr.const import MODE_WRITE
from mdr.messages import RequestFactory
from mdr.serial_thread import SerialThread


class Control:
    def __init__(self):
        self._rr_callback = None
        self.serial = SerialThread()
        self.rf = RequestFactory()

    def send_request(self, callback, name, *args):
        while self.serial.get_mode() != MODE_WRITE:
            self.serial.abort_current_task()
            print('send_request force abort', file=stderr)
            sleep(0.05)
        request = self.rf.get_request(name, *args)


    def stop(self):
        pass

    def abort(self):
        pass

    def set_RR_callback(self, callback):
        pass

