

class Message:
    def __init__(self):
        self.__rcv_bytes = 0
        self.__send_bytes = 0

    def __repr__(self):
        return '<{}>: 0x{}'.format(self.__class__.__name__, self.get_bytes().hex())

    def get_bytes(self):
        raise NotImplementedError('Implement in subclass')

    def inc_sent_count(self):
        self.__send_bytes = self.__send_bytes + 1

    def get_sent_count(self):
        return self.__send_bytes

    def inc_rcv_count(self):
        self.__rcv_bytes = self.__rcv_bytes + 1

    def get_rcv_count(self):
        return self.__rcv_bytes

    def expect_response(self):
        raise NotImplementedError('Implement in subclass')

    def get_delay(self):
        return 5


class BaseResponse:
    def __init__(self):
        self.response = bytearray()

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

    @classmethod
    def length(cls):
        raise NotImplementedError('Implement in subclass')

    @classmethod
    def signal_byte(cls):
        raise NotImplementedError('Implement in subclass')

    def add_byte(self, byte):
        self.response.append(byte)

    def get_bytes(self):
        return self.response

    def is_blocking(self):
        return False

    def process(self):
        raise NotImplementedError('Implement in subclass')
