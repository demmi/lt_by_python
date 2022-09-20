'''
4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата.

'''
print('_4.1_')
def square(a):
    perimetr = 4 * a
    ploshad = a * a
    diagonal = a * (2 ** (1 / 2))
    return perimetr, ploshad, diagonal

print(square(5))

'''
4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно 
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35 
	position: web developer
'''
print('_4.2_')
def take_args(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {str(value)}')
take_args(name='John', last_name='Smith', age=35, position='web developer')

'''
4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
     положительные числа
'''
print('_4.3_')
my_list = [20, -3, 15, 2, -1, -21]
print(list(filter(lambda x: x > 0, my_list)))


'''
4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
'''
print('_4.4_')
from functools import reduce
my_list = [20, 1, 2]
list_num = list(filter(lambda x: x > 0, my_list))
print(reduce(lambda x, y: x * y, list_num))


'''
4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле.
'''
print('_4.5_')
from hw_4_my_calc import *

x, y = 5, 3
print('Сумма =', summa(x, y))
print('Разность =', difference(x, y))
print('Умножение =', multiplication(x, y))
print('Деление =', subtraction(x, y))
print('Возведение в степень =', degree(x, y))