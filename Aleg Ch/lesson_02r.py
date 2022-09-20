# HomeWork 2
# -------------------- 2.1 --------------------
# health = 1
# if health > 0:
#     print('healthy')
# else:
#     print('not healthy')
# --------------
#
#
# def heals(x):
#     return x > 0
#
#
# print(heals(3))  # 3 - argument
# ---------------
# x = int(input('Enter your heals, number: '))
#
#
# def heals(x):
#     return x > 0
#
#
# if int(heals(x)) > 0:
#     print('healthy')
# else:
#     print('not healthy')
# -------------------- 2.2 --------------------
# x = 3
# if x % 2 == 0:
#     print(x, 'even')
# else:
#     print(x, 'odd')
# ---------------
# for x in range(4):
#     if x % 2 == 0:
#         print(x, 'even number')
#     else:
#         print(x, 'odd number')
#
# -------------------- 2.3 --------------------
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года,
# которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
# year = 1900
# if year % 4 == 0 and year % 100 != 0:
#     print(year, 'LEAP YEAR')
# elif year % 100 == 0 and year % 400 == 0:
#     print(year, 'LEAP YEAR')
# else:
#     print(year, 'common year')
# -------------------
# for year in range(1900, 2001):
#     if year % 4 == 0 and year % 100 != 0:
#         print(year, 'LEAP YEAR *')
#     elif year % 100 == 0 and year % 400 == 0:
#         print(year, 'LEAP YEAR *')
#     else:
#         print(year, 'common year')
# -------------------
# year = 1900
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(year, 'LEAP year')
# else:
#     print(year, 'common year')
# -------------------
# for year in range(1, 2025):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print(year, 'LEAP year')
#     else:
#         print(year, 'common year')
#
# ------------- Вложенные условия:
# year = 400
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, 'LEAP year')
#         else:
#             print(year, 'common year')
#     else:
#         print(year, 'common year')
# else:
#     print(year, 'common year')
#
# -------------------- 2.4 --------------------
# text = input('Enter your text: ')
# number = int(input('Enter number of copies: '))
# print((text + "\n") * number)
# --------------
# text = input('Enter your text: ')
# number = int(input('Enter number of copies: '))
# --------------
# i = 1
# while i <= number:
#     print(i, text)
#     i += 1
# --------------
# for i in range(number):
#     print(i + 1, text)
#
# **************************** REVIEW *****************************
# ------------ FOR
# for index in range(10):
#     print(index, end='')
# print()
# name = input('Enter text: ')
# print(len(name))    # сколько символов в name
# for letter in name:
#     print(letter, end=' ')  # вывод символов, end=' ' в строчку через пробел
# print()  # перевод строки
# for letter in range(len(name)):  # выведет позиции символов
#     print(letter, end=' ')
#
