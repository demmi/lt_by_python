# ---------- FUNCTIONS ----------

# def person(age, last_name, name):  # позиционные параметры
#     return f'Hello, my name is {name} {last_name}. I am {age} years old'
#
#
# print(person(30, 'Smith', 'Anna'))  # Hello, my name is Anna Smith. I am 30 years old
# print(person('Smith', 'Anna', 18))  # Hello, my name is 18 Anna. I am Smith years old - нарушен порядок аргументов :)


# def person(age, last_name='Smith', name='Anna'):  # два именованных параметра
#     return f'Hello, my name is {name} {last_name}. I am {age} years old'
#
#
# print(person(33))  # Hello, my name is Anna Smith. I am 33 years old - можно не указывать значения по умолчанию
# print(person(34, last_name='Price'))  # Hello, my name is Anna Price. I am 34 years old
# # print(person(last_name='Price', 34))  # SyntaxError: на 1-м месте д.б. ПОЗИЦИОННЫЙ аргумент!
# print(person(last_name='Price', age=34))  # для именованных аргументов порядок можно не соблюдать


# def pattern(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1
#
#
# print(pattern(char1='/', length=9))  # /*/*/*/*/*/*/*/*/*/

# ---------- ВСТРОЕННЫЕ ФУНКЦИИ (BUILT-IN FUNCTIONS) ----------
# min_arg = min(5, 6, 8, 10)
# print(min_arg)


# ---------- ПРОСТРАНСТВО ИМЕН (SCOPE) ----------
# x = 15
# y = 78
# def sum_it(x, y):
#     print(f'Locals: {locals()}')  # Locals: {'x': 5, 'y': 8}
#     return x + y
#
#
# print(f'Inside the function: {sum_it(5, 8)}')  # Inside the function: 13
# print(f'Outside the function: {x + y}')  # Outside the function: 93
# print(f'Globals: {globals()}')  # Globals: {тут покажет длинную строку - все о программе}

# ---------- ВСТРОЕННЫЕ МОДУЛИ (BUILT-IN MODULES) ----------
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

# ---------- lambda functions ----------
# lambda функция используется, когда ненадолго требуется безымянная функция, имеет лишь одно выражение

# print((lambda x, y: x * y)(5, 8))  # 40 - функция в 1 строчку и тут же передали аргументы

# mult = lambda x, y: x * y  # 40 - lambda функцию можно задать через переменную
# print(mult(5, 8))  # и вывести результат через переменную
#
#
# print('------Sum list_1 With function and for loop----------')
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# def filter_and_sum_nums(l):
#     new_l = []
#     for i in l:
#         if isinstance(i, int):
#             new_l.append(i)
#     return sum(new_l)
#
#
# print(filter_and_sum_nums(list_1))  # сумма чисел в списке 213
#
# print('--------Sum list_1 with lambda and filter----------')
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print(sum((filter(lambda x: isinstance(x, int), list_1))))  # сумма чисел в списке 213 - в 1 строку
#
#
#
# print('------Filter odd_nums with custom function----------')
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#
#
# def take_odd(num):
#     if isinstance(num, int) and num % 2:
#         return True
#     return False
#
#
# print(list(filter(take_odd, list_1)))  # [75] список нечетных чисел
#
# print('-----Filer odd_nums with lambda----------')
# filtered = list(filter(lambda x: isinstance(x, int), list_1))  # отфильтровали числа, в список
# print(list(filter(lambda x: x % 2, filtered)))  # а потом отфильтровали нечётные, в список
#
# list_3 = [1, 2, 5, 8, 10, 105, 78]  # если имеем другой список, однородный
# print(list(filter(take_odd, list_3)))  # то можем вызвать для него уже готовую функцию take_odd: [1, 5, 105]
#
# print(list(filter(lambda x: x % 2, list_3)))  # [1, 5, 105] то же для list_3 через lambda
#
# print('-----Filer strings with "a" using custom function ----------')
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# new_l = []
# for item in list_1:
#     if isinstance(item, str) and 'a' in item:
#         new_l.append(item)
# print(new_l)
#
# print('-----Filer strings with "a" using lambda ----------')
# filtered = list(filter(lambda x: isinstance(x, str), list_1))
# print(list(filter(lambda x: 'a' in x, filtered)))
# print(list(filter(lambda x: 'a' not in x, filtered)))  # ['Hi'] - слова, где нет 'a'
#
# --- но тут лучше методом list comprehension ---
# print([word for word in list_1 if type(word) == str if 'a' in word])  # ['ananas', 'pizza']
#
#
# -------------------- MODULES --------------------
# ///// 39:50
from functools import reduce
res = reduce(lambda x, y: x*y, [1, 5, 8, 11, 13])
print(res)
#
# import functools
# from functools import reduce
# res = reduce(lambda x, y: x*y, [1, 5, 8, 11, 13])
# print(res)
#
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
