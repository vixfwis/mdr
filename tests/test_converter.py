from mdr.utils.converter import to_float, from_float
import pytest


@pytest.mark.parametrize('array,value', [
    (bytearray.fromhex('2f440000'), 700.0),
    (bytearray.fromhex('96440000'), 1200.0),
    (bytearray.fromhex('23448f22'), 652.54),
])
def test_to_float(array, value):
    assert to_float(array) == pytest.approx(value)


@pytest.mark.parametrize('value,array', [
    (245, bytearray.fromhex('75430000')),
    (1.76, bytearray.fromhex('e13fae47')),
    (1554, bytearray.fromhex('c2440040')),
])
def test_from_float(value, array):
    assert from_float(value) == array