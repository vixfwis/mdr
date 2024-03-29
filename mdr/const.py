SPEED = {
    '200': 0,
    '70': 1,
    '30': 2,
    '10': 3,
    '3.3': 4,
    '1': 5,
    '0.6': 6
}

STEP = {
    '0.002': 0,
    '0.01': 1,
    '0.05': 2,
    '0.1': 3,
    '0.5': 4,
    '1': 5,
    '5': 6
}

MODE_READ = 0
MODE_WRITE = 1
ACK = bytes.fromhex('23')
ABORT = bytes.fromhex('89')
