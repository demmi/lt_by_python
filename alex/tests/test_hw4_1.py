import pytest
from alex.homework4_1 import *
from random import sample

test_cases = set(sample(range(12345678, 123456789), 20))


@pytest.mark.parametrize("num", test_cases)
def test_big_num_sums(num):
    assert big_num_sum1(num) == big_num_sum2(num)
