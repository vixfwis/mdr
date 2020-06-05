from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed
import serial


def scan_ports():
    pool = ThreadPoolExecutor()
    ports = [f'COM{i}' for i in range(1, 10)]
    futures = {pool.submit(check_port, p): p for p in ports}
    for f in as_completed(futures):
        port = futures[f]
        try:
            result = f.result()
        except Exception as exc:
            print(f'{port} generated an exception: {exc}')
        else:
            if result:
                return port


def check_port(port):
    ACK = bytes.fromhex('23')
    r1 = bytes.fromhex('2a')
    try:
        p = serial.serial_for_url(port, baudrate=19200,
            bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE, timeout=3)
        p.write(ACK)
        p.flush()
        b = p.read(1)
        p.close()
        del p
        if b == ACK or b == r1:
            return True
        return False
    except serial.SerialException as e:
        p = None
        del p
        return False
