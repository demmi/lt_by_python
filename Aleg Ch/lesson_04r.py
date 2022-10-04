# HomeWork 4
#
# == 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
#      (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
#
# side = (int(input('Enter the side length of the square: ')))  # 16
#
#
# def square(x):
#     return x * 4, x * x, (2 * (x ** 2)) ** 0.5
#
#
# print(square(side))  # (64, 256, 22.627416997969522)
#
# == 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит
#      их построчно в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
#
# def employees(**kwargs):
#     print('--- Result ---')
#     for key, value in kwargs.items():
#         print('{}: {}'.format(key, value))
#
#
# employees(name='John', last_name='Smith', age=35, position='web developer')
# --- Result ---
# name: John
# last_name: Smith
# age: 35
# position: web developer
#
# == 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
#      содержащий только положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# list_3 = list(map(lambda x: abs(x), my_list))
# print(list_3)  # [20, 3, 15, 2, 1, 21]
# ---
# list_3 = []
# for x in my_list:
#     list_3.append(abs(x))
# print(list_3)
# ---
# list_3 = [abs(x) for x in my_list]
# print(list_3)
#
# == 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# my_list = [20, -3, 15, 2, -1, -21]
# import functools  # импорт модуля functools
# res = functools.reduce(lambda x, y: x * y, my_list)
# print(res)  # -37800
# ---
# import math
# print(math.prod(my_list))
#
# == 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические
#      вычисления. Примените эти функции в качестве методов в другом файле.
# import my_calc
# print(my_calc.sum_it(3, 5))  # 8 сумма
# print(my_calc.sub(23, 19))  # 4 разность
# print(my_calc.prod(7, 9))  # 63 произведение
# print(my_calc.div(33, 11))  # 3.0 частное
# print(round(my_calc.per(23, 114), 2))  # 26.22 процент x от y
