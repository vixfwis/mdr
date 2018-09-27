from mdr.utils.converter import from_float
from ..message import Message as __Message


class SetWaveLength(__Message):
    def expect_response(self):
        return True

    def __init__(self, wave_length):
        super().__init__()
        self.wl = wave_length

    def __repr__(self):
        return 'set-wave-length %f' % self.wl

    def get_bytes(self):
        b = bytearray.fromhex('80')
        for byte in from_float(self.wl):
            b.append(byte)
        return b


class SetWaveLengthWO(__Message):
    def expect_response(self):
        return True

    def __init__(self, wave_length):
        super().__init__()
        self.wl = wave_length

    def __repr__(self):
        return 'set-wave-length-wo %f' % self.wl

    def get_bytes(self):
        b = bytearray.fromhex('90')
        for byte in from_float(self.wl):
            b.append(byte)
        return b


class Measure(__Message):
    def expect_response(self):
        return True

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'measure'

    def get_bytes(self):
        return bytearray.fromhex('95')
