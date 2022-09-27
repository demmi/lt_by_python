import pytest

from AndreyHerasimchyk.HW.hw4 import square, only_positive, mult_positive, print_kwargs
from AndreyHerasimchyk.HW.my_calc import sum_, sub_, mult_, div_


def test_square():
    assert square(10) == (40, 100, 14.14)  # add assertion here


def test_only_positive():
    assert only_positive([20, -3, 15, 2, -1, -21]) == [20, 15, 2]


def test_mult_positive():
    assert mult_positive([20, -3, 15, 2, -1, -21]) == 600


def test_print_kwargs():
    assert print_kwargs(name="John", last_name="Silver", age=35,
                        position="Python developer") == 'name: John\nlast_name: Silver\nage: 35\nposition: Python developer\n'


cases = ((5, 10), (-1, 7), (0, 15), (15, 0), (-100, -55), (11, 4), (23, -12))


@pytest.mark.parametrize('a, b', cases)
def test_sum_(a, b):
    assert sum_(a, b) == a + b


@pytest.mark.parametrize('a, b', cases)
def test_sub_(a, b):
    assert sub_(a, b) == a - b


@pytest.mark.parametrize('a, b', cases)
def test_mult_(a, b):
    assert mult_(a, b) == a * b


@pytest.mark.parametrize('a, b', cases)
def test_div_(a, b):
    if b:
        assert div_(a, b) == a / b
    else:
        assert div_(a, b) == 'На ноль делить нельзя'
