# HomeWork 3
#
# ==---------- 3.1 ----------
# Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])  # [1, 2, 3]
#
# ==---------- 3.2 ----------
# - получите сумму всех чисел,
# - распечатайте все строки, где есть буква 'a'
#
# list_2 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# lst2 = [x for x in list_2 if type(x) == int]
# print(lst2)  # [2, 75, 36, 100]
# print(sum(lst2))  # - сумма всех чисел 213
# print(sum([x for x in list_2 if type(x) == int]))  # или так, в одну строку
# -----
# for word in list_2:
#     if type(word) == str and 'a' in word:
#         print(word)
# ananas
# pizza
#
# lst2a = [word for word in list_2 if type(word) == str if 'a' in word]
# print(lst2a)  # ['ananas', 'pizza']
#
# ==---------- 3.3. ----------
# Превратите лист в кортеж
# list_3 = ['cat', 'dog', 'horse', 'cow']
# tuple_3 = tuple(list_3)
# print(tuple_3)
#
# ==---------- 3.4. ----------
# Напишите программу, которая определяет, какая семья больше.
# 1) Программа имеет два input() - например, family_1, family_2.
# 2) Членов семьи нужно перечислить через запятую.
# Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = input('family_1: ')
# f1 = tuple(family_1.split(','))
# family_2 = input('family_2: ')
# f2 = tuple(family_2.split(','))
# if len(f1) > len(f2):
#     print(family_1)
# elif len(f1) < len(f2):
#     print(family_2)
# else:
#     print('Equal')
#
# ==---------- 3.5. ----------
# Создайте словарь film c ключами title, director, year, budget, slogan.
# В значения можете передать информацию о вашем любимом фильме
# - распечатайте только ключи
# - распечатайте только значения
# - распечатайте пары ключ - значение
#
# film = {
#     'title': 'Зеленая миля',
#     'director': 'Фрэнк Дарабонт',
#     'year': 1999,
#     'budget, $': 60000000,
#     'main_actor': 'Том Хэнкс',
#     'slogan': '«Пол Эджкомб не верил в чудеса. Пока не столкнулся с одним из них»'
# }
# print(film.keys())
# print(film.values())
# print(film)
#
# ==---------- 3.6 ----------
# Найдите сумму всех значений в словаре
# my_dict = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dict.values()))
# # ---
# result = 0
# for x in my_dict:
#     result += my_dict[x]  # my_dict[x] - доступ к значениям
# print(result)
#
# ==---------- 3.7 ----------
# Удалите повторяющиеся значения из списка
# list_7 = [1, 2, 3, 4, 5, 3, 2, 1]
# print({1, 2, 3, 4, 5, 3, 2, 1})
# ---
# lst_7 = set(list_7)
# print(lst_7)
#
# ==---------- 3.8 ----------
# Даны два множества
# - найдите значения, которые встречаются в обоих множествах
# - найдите значения, которые не встречаются в обоих множествах
# - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))  # {1, 100, 5, 9, 'z'}
print(set1.symmetric_difference(set2))  # {'a', 8, 'b', 12, 785, 21, 'l'}
print(set1.difference(set2), set2.difference(set1))  # {'a', 'b', 12} {8, 785, 'l', 21}
print(set1.issubset(set2))  # False
print(set2.issubset(set1))  # False
