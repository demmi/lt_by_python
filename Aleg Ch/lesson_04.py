# ВСТРОЕННЫЕ ФУНКЦИИ (BUILT-IN FUNCTIONS)
min_arg = min(5, 6, 8, 10)
print(min_arg)
#
# FUNCTIONS

# def person(age, last_name='Smith', name='Anna'):
#     return 'Hello, my name is' {name} {last_name}. I am {age} years old'
#
# print(person(name='Alce', age=30))


# def pattern(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1
#
# print(pattern(char1='*', length=9))


# ПРОСТРАНСТВО ИМЕН (SCOPE)
# x = 15
# y = 78
# def sum_it(x, y):
#     print(f'Locals: {locals()}')
#     return x + y
#
# print(f'Inside the function: {sum_it(5, 8)}')
# print(f'Outside the function: {x + y}')
# print(f'Globals: {globals()}')

# ВСТРОЕННЫЕ МОДУЛИ (BUILT-IN MODULES)
# from math import *
# import math as m
#
# arr = [1, 2, 3, 4, 5, 10, 25]
# new_arr = m.prod(arr)
# print(new_arr)

# import datetime
# birth_year = 1980
# current_date = datetime.date.today()
# current_age = current_date.year - birth_year
# current_month = current_date.month
# print(current_date)
# print(current_age)
# print(current_month)

# lambda functions
# mult = lambda x, y: x*y
# print(mult(5, 8))

#
# print(f(4, 2))
#
#
# print('------Sum list_1 With function and for loop----------')
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# def filter_and_sum_nums(l):
#     new_l = []
#     for i in l:
#         if isinstance(i, int):
#             new_l.append(i)
#     return sum(new_l)
#
#
# print(filter_and_sum_nums(list_1))
#
# print('--------Sum list_1 with lambda and filter----------')
# print(sum((filter(lambda x: isinstance(x, int), list_1))))
#
#
# print('------Filter odd_nums with custom function----------')
# def take_odd(num):
#     if isinstance(num, int) and num%2:
#         return True
#     return False
#
# print(list(filter(take_odd, list_1)))
#
# list_3 = [1, 2, 5, 8, 10, 105, 78]
# print(list(filter(take_odd, list_3)))
#
# print('-----Filer odd_nums with lambda----------')
# filtered = list(filter(lambda x: isinstance(x, int), list_1))
# print(list(filter(lambda x: x%2, filtered)))
#
# print(list(filter(lambda x: x%2, list_3)))
#
# print('-----Filer strings with "a" using custom function ----------')
# new_l = []
# for item in list_1:
#     if isinstance(item, str) and 'a' in item:
#         new_l.append(item)
# print(new_l)
# #
# print('-----Filer strings with "a" using lambda ----------')
# filtered = list(filter(lambda x: isinstance(x, str), list_1))
# print(list(filter(lambda x: 'a' in x, filtered)))

# MODULES
# import functools
# from functools import reduce
# res = reduce(lambda x, y: x*y, [1, 5, 8, 11, 13])
# print(res)
#
# from my_file import *
# res = sum_it(5, 8)
# print(res)
#
# res1 = prod(5, 8)
# print(res1)
#
# from my_file import *
# def tests():
#     assert sum_it(5, 8) == 13, f'Wrong number, actual result is {sum_it(5, 8)}'
#     assert prod(10, 6) == 60, f'Wrong number, actual result is {prod(10, 6)}'
#     assert div(10, 0) == "Can't divide by zero"
#
# tests()

# def sum_it(**kwargs):
#     print(type(kwargs))
#     return sum(kwargs.values())
#
# print(sum_it(num1=4, num2=5, num3=10))
#
# def sum_i(*args):
#     print(type(args))
#     return sum(args)
# print(sum_i(5, 6, 10))
#
# list_2 = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x*x, list_2)))
# print([x*x for x in list_2])
