from concurrent.futures.thread import ThreadPoolExecutor

import serial


def find_port():
    pool = ThreadPoolExecutor()


def check_port(port):
    ACK = bytes.fromhex('23')
    try:
        p = serial.serial_for_url(
            port,
            baudrate=19200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=3,
        )
        p.write(ACK)
        p.flush()
        b = p.read(1)
        print(b)
        if b == ACK:
            return True
        return None
    except serial.SerialException as e:
        p = None
        del p
        return None
