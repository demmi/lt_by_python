# Операторы сравнения, логические, условные. Циклы. Определение функции.
# print(5 == 5)  # True
# print(5 != 5)  # False
# print(5 > 3)  # True
# print(5 + 2 == 9)  # False
#
# x = 5
# print(x > 2 and x < 8)  # True
# print(x > 2 and x > 8)  # False
# print(x > 2 or x > 8)  # True
# print(x < 2 or x > 8)  # False
# print(not x > 5)  # True
# print(not x != 5)  # True
# print(not x == 5)  # False
# print(x > 2 and not x > 8)  # True
# print(x < 2 or not x < 8)  # False
#
# x = 5
# if x == 5:
#     print('five')
# elif x > 5:
#     print('more than five')
# else:
#     print('less than five')
#
# x = 6
# message = ''
# if x == 5:
#     message = 'five'
# elif x != 5:
#     message = 'not five'
# print(message)
#
# -------------------- CYCLE while --------------------
# i = 1
# while i < 4:
#     print(i, 'Hello!')
#     i += 1  # то же самое i = i + 1
#
# i = 0
# while i < 5:
#     if i == 3:        # После вывода "3 О!" остановка цикла
#         break
#     i = i + 1
#     print(i, 'O!')
#
# i = 0
# while i < 5:
#     i = i + 1
#     if i == 3:      # То же самое одной строкой, без continue: if i != 3:
#         continue    # continue выполняет переход к следующей итерации цикла
#     print(i)
# print('---')
#
# var = 6
# while var > 1:
#     var = var - 1     # Обратный отстчет
#     if var == 3:      # Пропуск тройки, переход к следующей итерации
#         continue
#     print('Current variable value :', var)
# print('Good bye!' + '\n')
#
# i = 5
# while i > 0:
#     print(i)
#     i = i - 1  # Обратный отстчет
# print('Go!')
#
# -------------------- CYCLE for --------------------
#
# name = input('Enter your name: ')
# for letter in name:  # for перебирает name по символам и не требует условий
#     print(letter)  # letter - просто временная переменная
# Распеатка вертикальная - с переводом строки
#
# for letter in 'Python':
#     if letter == 'h':
#         continue  # Пропускается 'h'
#     print('Current Letter :', letter)
#
# name = input('Enter your name: ')
# for letter in name:
#     print(letter, end=' ')  # end отменяет перевод строки, =' ' - добавляет пробел
# ----------------
#
# name = "Oleg"
# print(name[0])  # выведет первую букву - индексация наинается с нуля
# print(name[-1])  # выведет последнюю букву
#
# for i in range(3):  # range(3) - повторение цикла 3 раза: 0, 1, 2
#     print(i)
# for i in range(1, 10, 2):  # start 1, stop 10, step 2 - нечетные числа от 1 до 9
#     print(i)
# Верхняя граница диапазона не включается!
#
# for i in range(5, 1, -1):  # start 5, stop 1, step -1 - обратный отсчет от 5 до 2
#     print(i)
#
# for i in range(1, 4):  # start 1, stop 4, step по умоланию 1 - отсчет от 1 до 3
#     print(i)
#
# for i in range(-3, 0):
#     print(i)
#
# for i in range(0, -4, -1):
#     print(i)
#
# for num in range(2, 10):
#     if num % 2 == 0:        # если переменная чётная even
#         print("Found an even number", num)  # печатаем "Найдено чётное число, num"
#         continue            # для чётных пропускаем команду print("Found a number", num)
#     print("Found a number", num)
#
# name = '' or 0 or None or []
# print(bool(name))  # Пустая строка, 0, None, [] (пустой список) = False
# name = 'Oleg'
# print(bool(name))  # = True
# ----- Это используется для проверки, задано ли значение переменной:
# i = ''
# if i:    # означает: если i задано
#     print('true')
# else:
#     print('false')
#
# ----- Напишем программу проверки возраста:
# age = int(input('Enter your age: '))
# if age < 13:
#     print('Where\'s your mom?')
# elif age < 21:
#     print('Go home, baby!')
# elif age >= 100:
#     print('A you sure?')
# else:
#     print('You may enter')
#
# -------------------- FUNCTIONS --------------------
# def func(x, n):  # задаем параметры x, n
#     return x ** n  # return возвращает результат вычисления
#
#
# print(func(5, 2))  # вызываем функцию, задаем аргументы 5, 2, print результат 25
# print(func(2, 4))  # задаем аргументы (2, 4): 2 ** 4 == 16
#
#
# def y(x, n):
#     print(x + n)  # вместо return сразу print
#
#
# y(3, 2)  # тогда здесь только вызываем функцию
#
#
# def y(x, n):
#     return x / n  # вместо return сразу print
#
#
# print(y(int(input('enter x: ')), int(input('enter n: '))))  # аргументы задаем через input
#
#
# def c(a, b):
#     return a - b
#
#
# a = int(input('enter a: '))
# b = int(input('enter b: '))
#
#
# print(c(a, b))
#
# symbol = '*'
# print(symbol*20)
