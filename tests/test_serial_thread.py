import logging

from mdr.messages import Message
from mdr.serial_thread import SerialThread
from unittest.mock import patch
from time import sleep


def test_serial_connect():
    serial = SerialThread(port='loop://')
    serial.setDaemon(True)
    serial.logger.setLevel(logging.DEBUG)
    serial.start()
    sleep(0.1)  # wait for thread start
    assert serial.connected
    serial.stop()
    serial.join(timeout=1)
    assert not serial.is_alive()


@patch('mdr.messages.Message.get_bytes', return_value=bytearray.fromhex('23'))
@patch('mdr.messages.factories.ResponseFactory.submit')
@patch('mdr.messages.Message.expect_response', return_value=True)
def test_serial_message(*args, **kwargs):
    serial = SerialThread(port='loop://')
    serial.setDaemon(True)
    serial.logger.setLevel(logging.DEBUG)
    serial.start()
    sleep(0.1)  # wait for thread start
    msg = Message()
    serial.requests.put(msg)
    sleep(0.1)  # wait for queues/request processing
    assert msg.get_sent_count() == 1
    serial.serial_port.write(bytes.fromhex('10'))  # inject some test response
    sleep(0.1)  # threads...
    assert msg.get_rcv_count() >= 1
    sleep(0.1)
    assert serial.get_mode() == serial.MODE_WRITE
