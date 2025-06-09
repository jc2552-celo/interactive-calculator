import pytest
from calculator import operations

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 5, 5)
])
def test_add(a, b, expected):
    assert operations.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0)
])
def test_subtract(a, b, expected):
    assert operations.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-2, -3, 6)
])
def test_multiply(a, b, expected):
    assert operations.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (1, 2, 0.5)
])
def test_divide(a, b, expected):
    assert operations.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        operations.divide(5, 0)
