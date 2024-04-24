from src.ops import *


def test_add():
    assert add(3, 3) == 5


def test_subtract():
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(10, 5) == 2


def test_cal():
    assert cal(12,3,3) == 5
