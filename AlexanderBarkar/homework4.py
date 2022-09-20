from math import sqrt
from functools import reduce
from my_calc import *

"""4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): 
     периметр квадрата, площадь квадрата и диагональ квадрата.

4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно 
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35 
	position: web developer

4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только 
     положительные числа

4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке 
4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления. 
     Примените эти функции в качестве методов в другом файле. """


def square(square_side: int) -> tuple:
    return square_side * 4, square_side**2, square_side * sqrt(2)


print("-" * 10 + " Task 4.1 " + "-" * 10)
print(square(2))
print(square(5))

print("-" * 10 + " Task 4.2 " + "-" * 10)


def print_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {str(value)}")


print_args(name="John", last_name="Smith", age=35, position="web developer")
print("-" * 10)
print_args(
    title="Достучаться до небес",
    director="Thomas Jahn",
    year=1997,
    budget=2200000,
    main_actor="Til Schweiger",
    slogan="Быстрый автомобиль, миллион марок в багажнике, и всего одна неделя жить",
)

print("-" * 10 + " Task 4.3 " + "-" * 10)
my_list = [20, -3, 15, 2, -1, -21]
print(f"Initial list: {my_list}")
my_list_pos = list(filter(lambda x: x > 0, my_list))
print(f"Positive values: {my_list_pos}")
my_list_mul = reduce(lambda x, y: x * y, my_list)
print(f"Multiplication result: {my_list_mul}")

print("-" * 10 + " Task 4.4 " + "-" * 10)
print(sum_(10, 35))
print(sub_(87, 11))
print(mul_(2, 17))
print(div_(128, 2))
print(pow_(2, 10))
print(div_(12, 0))
