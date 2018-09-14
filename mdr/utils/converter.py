from struct import pack, unpack


def to_float(b):
    """
    Convert 4 bytes from bytearray to float
    :type b: bytearray
    :rtype: float
    """
    arr = b[:4]
    b1, b2 = arr[0], arr[1]
    arr[0], arr[1] = arr[2], arr[3]
    arr[2], arr[3] = b1, b2
    return unpack('f', arr)[0]


def from_float(f):
    """
    Convert float to 4 bytes bytearray
    :type f: float
    :rtype: bytearray
    """
    arr = bytearray(pack('f', f))
    b1, b2 = arr[0], arr[1]
    arr[0], arr[1] = arr[2], arr[3]
    arr[2], arr[3] = b1, b2
    return arr
