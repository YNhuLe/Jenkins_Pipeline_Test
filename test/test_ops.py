from src.ops import OPS


def test_add():
    result = OPS.add(2, 3)
    assert result == 5


def test_subtract():
    result = OPS.subtract(2, 3)
    assert result == -1


def test_multiply():
    result = OPS.multiply(2, 3)
    assert result == 6


def test_divide():
    result = OPS.divide(10, 5)
    assert result == 2


def test_cal():
    result = OPS.cal(12, 3, 3)
    assert result == 5


def test_percentage():
    result = OPS.percentage(2, 10)
    assert result == 20
