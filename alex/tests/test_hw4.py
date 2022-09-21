import pytest
from alex.my_calc import *

test_cases = ((1, 2), (3, 4), (-1, 4), (3, -10), (10, 0), (0, 6), (-4, 2), (18, -7))


@pytest.mark.parametrize("a, b", test_cases)
def test_sum_(a, b):
    assert sum_(a, b) == a + b


@pytest.mark.parametrize("a, b", test_cases)
def test_sub_(a, b):
    assert sub_(a, b) == a - b


@pytest.mark.parametrize("a, b", test_cases)
def test_mul_(a, b):
    assert mul_(a, b) == a * b


@pytest.mark.parametrize("a, b", test_cases)
def test_div_(a, b):
    if b:
        assert div_(a, b) == a / b
    else:
        assert div_(a, b) == "ZeroDivisionError('division by zero')"


@pytest.mark.parametrize("a, b", test_cases)
def test_pow_(a, b):
    assert pow_(a, b) == a**b
