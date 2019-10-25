from struct import pack, unpack
from math import trunc


def to_float(b):
    arr = b[:4]
    b1, b2 = arr[0], arr[1]
    arr[0], arr[1] = arr[2], arr[3]
    arr[2], arr[3] = b1, b2
    return unpack('f', arr)[0]


def from_float(f):
    arr = bytearray(pack('f', f))
    b1, b2 = arr[0], arr[1]
    arr[0], arr[1] = arr[2], arr[3]
    arr[2], arr[3] = b1, b2
    return arr


def from_short(s):
    return bytearray(pack('h', s))


def get_scan_array_len(start, end, step):
    return int(trunc((end-start)/(step*2)))
