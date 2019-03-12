from mdr.utils.converter import from_float, from_short
from ..message import Message as __Message
from ..responses import responses as resp


class SetWaveLength(__Message):
    def expect_response(self):
        return resp.Ready

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
        return resp.Ready

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
        return resp.GetFloatValue

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'measure'

    def get_bytes(self):
        return bytearray.fromhex('95')


class Calibrate(__Message):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'calibrate'

    def expect_response(self):
        return resp.Ready

    def get_bytes(self):
        #return bytearray.fromhex('84018500000000')
        return bytearray.fromhex('8b0b8c018d0084018500000000')


class SetVoltage(__Message):
    def __init__(self, app, voltage):
        super().__init__()
        self.app = app
        self.voltage = voltage

    def __repr__(self):
        return 'set-voltage'

    def expect_response(self):
        return None

    def get_bytes(self):
        if self.app == 1:  # ФЭУ-100
            request = bytearray.fromhex('82')
        elif self.app == 2:  # ФЭУ-62
            request = bytearray.fromhex('83')
        else:
            raise AttributeError('Wrong input params')
        for b in from_float(self.voltage):
            request.append(b)
        return request


class MonoScan(__Message):
    def __init__(self, start, end, step, speed, empty, array_length):
        super().__init__()
        self.start = start
        self.end = end
        self.step = step
        self.speed = speed
        self.empty = empty
        self.array_length = array_length

    def __repr__(self):
        return 'mono-scan'

    def expect_response(self):
        return resp.GetFloatValue

    def get_bytes(self):
        request = bytearray.fromhex('97')
        for b in from_float(self.start):
            request.append(b)
        for b in from_float(self.end):
            request.append(b)
        request.append(self.step)
        request.append(self.speed)
        for b in from_short(self.empty):
            request.append(b)
        for b in from_short(self.array_length):
            request.append(b)
        request.append(bytes.fromhex('81')[0])
        request.append(1)
        return request


class SetFilter(__Message):
    def __init__(self, fnum):
        super().__init__()
        self.filter = fnum

    def expect_response(self):
        return resp.Ready

    def get_bytes(self):
        request = bytearray.fromhex('88')
        request.append(self.filter)
        return request


class SetChange(__Message):
    def __init__(self, first, second):
        super().__init__()
        self.first = first
        self.second = second

    def expect_response(self):
        return None

    def get_bytes(self):
        request = bytearray.fromhex('8e')
        for b in from_float(self.first):
            request.append(b)
        for b in from_float(self.second):
            request.append(b)


class ManualStop(__Message):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'manual-stop'

    def expect_response(self):
        return resp.Ready

    def get_bytes(self):
        return bytearray.fromhex('8a01')


class ManualForward(__Message):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'manual-forward'

    def expect_response(self):
        return resp.Ready

    def get_bytes(self):
        return bytearray.fromhex('8a03')


class ManualReverse(__Message):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'manual-reverse'

    def expect_response(self):
        return resp.Ready

    def get_bytes(self):
        return bytearray.fromhex('8a02')


class ManualEndMode(__Message):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'manual-end-mode'

    def expect_response(self):
        return resp.Ready

    def get_bytes(self):
        return bytearray.fromhex('8a04')


class ManualBeginMode(__Message):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'manual-begin-mode'

    def expect_response(self):
        return resp.Ready

    def get_bytes(self):
        return bytearray.fromhex('8a05')


class ManualGetWaveLength(__Message):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'manual-get-wave-length'

    def expect_response(self):
        return resp.GetWaveLength

    def get_bytes(self):
        return bytearray.fromhex('8a06')


class ManualFaster(__Message):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'manual-faster'

    def expect_response(self):
        return resp.Ready

    def get_bytes(self):
        return bytearray.fromhex('8f01')


class ManualSlower(__Message):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'manual-slower'

    def expect_response(self):
        return resp.Ready

    def get_bytes(self):
        return bytearray.fromhex('8f02')
