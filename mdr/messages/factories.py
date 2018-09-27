import logging
from importlib import import_module
from queue import Queue
from inspect import signature
from threading import Event


class ResponseFactory:
    def __init__(self):
        self.response_classes = import_module('mdr.messages.responses').__imported_classes__
        self.current_response = None
        self.remaining_bytes = 0
        self.logger = logging.getLogger(self.__class__.__name__)
        self.blocking_event = Event()
        self.continue_event = Event()
        self.responses = Queue()

    def submit(self, byte):
        self.logger.debug('Received byte %i' % byte)
        if self.current_response is None:
            self.logger.debug('Trying to find correct response class')
            self.current_response = self.find_response_class(byte)()
            self.logger.debug('Class found: %s' % str(self.current_response))
            self.remaining_bytes = self.current_response.length()
        else:
            self.current_response.add_byte(byte)
            self.remaining_bytes = self.remaining_bytes - 1
            self.logger.debug('Added byte to response object, remaining: %i' % self.remaining_bytes)
        if self.remaining_bytes == 0:
            self.logger.debug('Adding finished response to queue')
            self.responses.put(self.current_response)
            if self.current_response.is_blocking():
                self.logger.debug('Response is blocking, waiting for event...')
                self.blocking_event.set()
                self.continue_event.wait()
                self.logger.debug('Event set. Cleaning up...')
                self.blocking_event.clear()
                self.continue_event.clear()
            self.current_response = None

    def find_response_class(self, byte):
        for r in self.response_classes:
            if r.signal_byte()[0] == byte:
                return r
        raise ClassNotFound('Response class not found for signal byte {}'.format(bytes([byte]).hex()))


class RequestFactory:
    def __init__(self):
        self.__request_classes = {v.__name__: v for v in import_module('mdr.messages.requests').__imported_classes__}

    def get_request_list(self):
        return list(self.__request_classes.keys())

    def get_request_args(self, name):
        request = self.__request_classes[name]
        sig = signature(request.__init__)
        return list(sig.parameters.keys())[1:]

    def get_request(self, name, *args):
        return self.__request_classes[name](*args)


class ClassNotFound(Exception):
    pass
