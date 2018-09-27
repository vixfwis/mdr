import logging
from threading import Thread
from time import sleep

import pytest


@pytest.fixture
def rf():
    from mdr.messages import ResponseFactory
    factory = ResponseFactory()
    factory.logger.setLevel(logging.DEBUG)
    return factory


def test_ready_response(rf):
    for b in bytes.fromhex('82'):
        rf.submit(b)
    r = rf.responses.get()
    assert r.process()

@pytest.mark.parametrize('value,array', [
    (245, bytearray.fromhex('8075430000')),
    (1554, bytearray.fromhex('87c2440040')),
])
def test_get_float_value(rf, value, array):
    for b in array:
        rf.submit(b)
    r = rf.responses.get()
    assert r.process() == pytest.approx(value)


@pytest.mark.parametrize('request_message,array', [
    ('решетку', bytearray.fromhex('8302')),
    ('приемник', bytearray.fromhex('8401')),
    ('турель', bytearray.fromhex('8501')),
])
def test_blocking_response(rf, request_message, array):
    class BlockedThread(Thread):
        def __init__(self):
            super(BlockedThread, self).__init__()
            self.rf = rf
            self.array = array

        def run(self):
            for b in array:
                rf.submit(b)
    t = BlockedThread()
    t.setDaemon(True)
    t.start()
    sleep(0.1)  # wait for block
    assert t.rf.blocking_event.is_set()
    msg = t.rf.responses.get()
    assert request_message in msg.process()
    t.rf.continue_event.set()  # continue
    sleep(0.1)  # wait for thread to wake up
    assert not t.rf.blocking_event.is_set()


@pytest.mark.parametrize('values,array', [
    ([255, 0], bytearray.fromhex('8aff00')),
    ([165, 177], bytearray.fromhex('8aa5b1')),
])
def test_get_refs(rf, values, array):
    for b in array:
        rf.submit(b)
    r = rf.responses.get()
    assert r.process() == values
