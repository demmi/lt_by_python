from AndreyHerasimchyk.HW.hw4 import square, only_positive, mult_positive, print_kwargs


def test_square():
    assert square(10) == (40, 100, 14.14)  # add assertion here


def test_only_positive():
    assert only_positive([20, -3, 15, 2, -1, -21]) == [20, 15, 2]


def test_mult_positive():
    assert mult_positive([20, -3, 15, 2, -1, -21]) == 600


def test_print_kwargs():
    assert print_kwargs(name="John", last_name="Silver", age=35, position="Python developer") == 'name: John\nlast_name: Silver\nage: 35\nposition: Python developer\n'
