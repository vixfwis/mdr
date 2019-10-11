from mdr.utils.converter import to_float

from ..message import BaseResponse as __BaseResponse


class Ready(__BaseResponse):
    def __init__(self):
        super(Ready, self).__init__()

    def process(self):
        return True

    @classmethod
    def length(cls):
        return 0

    @classmethod
    def signal_byte(cls):
        return bytes.fromhex('82')


class GetFloatValue(__BaseResponse):
    def __init__(self):
        super(GetFloatValue, self).__init__()

    def process(self):
        return to_float(self.get_bytes())

    @classmethod
    def length(cls):
        return 4

    @classmethod
    def signal_byte(cls):
        return bytes.fromhex('80')

    
class RequestSetGrating(__BaseResponse):
    GRATING = {
        1: '3000 штр/мм',
        2: '1500 штр/мм',
        3: '750 штр/мм',
        4: '600 штр/мм',
        5: '300 штр/мм',
        6: '150 штр/мм',
        7: '75 штр/мм',
        8: '37.5 штр/мм',
    }

    def __init__(self):
        super(RequestSetGrating, self).__init__()

    @classmethod
    def length(cls):
        return 1

    def process(self):
        return 'Установите решетку %s' % self.GRATING[self.get_bytes()[0]]

    def is_blocking(self):
        return True

    @classmethod
    def signal_byte(cls):
        return bytes.fromhex('83')


class RequestSetPEM(__BaseResponse):
    PEM = {
        1: 'ФЭУ-100',
        2: 'ФЭУ-62',
        3: 'F',
        4: 'F'
    }

    def __init__(self):
        super(RequestSetPEM, self).__init__()

    @classmethod
    def length(cls):
        return 1

    def process(self):
        return 'Установите приемник %s' % self.PEM[self.get_bytes()[0]]

    def is_blocking(self):
        return True

    @classmethod
    def signal_byte(cls):
        return bytes.fromhex('84')


class RequestSetFilters(__BaseResponse):
    def __init__(self):
        super(RequestSetFilters, self).__init__()

    @classmethod
    def length(cls):
        return 1

    def process(self):
        return 'Установите %i турель фильтров' % self.get_bytes()[0]

    def is_blocking(self):
        return True

    @classmethod
    def signal_byte(cls):
        return bytes.fromhex('85')


class GetWaveLength(__BaseResponse):
    def __init__(self):
        super(GetWaveLength, self).__init__()

    def process(self):
        return to_float(self.get_bytes())

    @classmethod
    def length(cls):
        return 4

    @classmethod
    def signal_byte(cls):
        return bytes.fromhex('87')


class GetRefPoints(__BaseResponse):
    def __init__(self):
        super(GetRefPoints, self).__init__()

    def process(self):
        return [b for b in self.get_bytes()]

    @classmethod
    def length(cls):
        return 2

    @classmethod
    def signal_byte(cls):
        return bytes.fromhex('8a')
