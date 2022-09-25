#4.1 Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#     периметр квадрата, площадь квадрата и диагональ квадрата.


# import math
#
# def square(a):
#     perim = a*4
#     sq = a*a
#     diag = math.sqrt(2*(a**a))
#     return (perim, sq, diag)
#
# square(3)

#4.2 Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно в формате
# аргумент: значение. Например:
	# name: John
	# last_name: Smith
	# age: 35
	# position: web developer

# def employee(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# employee(name='John', last_name='Smith', age=35, position='web developer')

#4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#     положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x>0, my_list))
# print(new_list)

#4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# print(reduce(lambda x, y: x*y, my_list))



#4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#     Примените эти функции в качестве методов в другом файле.

from my_calc import *

print(add(5,6))
print(minus(6,5))
print(multi(5,6))
print(divide(6,0))