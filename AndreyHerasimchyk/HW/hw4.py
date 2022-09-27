# 4.1
from functools import reduce
# import my_calc


def square(length):
    return length * 4, length ** 2, round((2 ** 0.5) * length, 2)


# print(square(10))


# 4.2
def print_kwargs(**kwargs):
    # [print(f'{k}: {v}') for k, v in kwargs.items()]
    result = ''
    for k, v in kwargs.items():
        result += f'{k}: {v}\n'
    return result

print(print_kwargs(name="John", last_name="Silver", age=35, position="Python developer"))

# 4.3
my_list = [20, -3, 15, 2, -1, -21]


def only_positive(m):
    return list(filter(lambda x: x > 0, m))


mult_positive = lambda a: reduce(lambda x, y: x * y, only_positive(a))

# print(only_positive(my_list))
# print(mult_positive(my_list))

# 4.4
# print(my_calc.sum_(1, 2))
# print(my_calc.sub_(10, 5))
# print(my_calc.mult_(5, 11))
# print(my_calc.div_(20, 5))
# print(my_calc.div_(20, 0))
