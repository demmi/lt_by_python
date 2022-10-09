import os
import math
import re

# def user_friendly_size(file_size):
#     sizes = {40: 'TB', 30: 'GB', 20: 'MB', 10: 'kB', 0: 'B'}
#     if isinstance(file_size, str):
#         file_size = os.stat(file_size).st_size
#     for power, symbol in sizes.items():
#         if file_size // 2 ** power:
#             return f'{file_size / 2 ** power:.2f} {symbol}'


def user_friendly_size(file_size) -> str:
    symbols = ("B", "kB", "MB", "GB", "TB")
    if isinstance(file_size, str):  # Если аргумент - строка
        if file_size.isdigit():  # Если протупили и отправили число строкой
            file_size = int(file_size)
        else:
            file_size = os.stat(file_size).st_size  # Получим размер файла в байтах
    sym_index = int(math.log(file_size, 2) // 10)
    return f"{file_size / 2 ** (sym_index * 10):.2f} {symbols[sym_index]}"


# def counting_valleys(s):
#     val = lev = 0
#     for ch in s:
#         if ch == 'U':
#             lev += 1
#             if lev == 0:
#                 val += 1
#         if ch == 'D':
#             lev -= 1
#             if lev == -1:
#                 val += 1
#     return (val // 2)


def counting_valleys(s):
    valley = level = 0
    for path in s:
        level += {"F": 0, "U": 1, "D": -1}[path]
        if level == 0 and path == "U":
            valley += 1
    return valley


# a = 234042163/(2**24)
# print(a)
# print("%.2f" % a)
# print(round(a, 2))
# print("%.2f" % round(a, 2))
# print("{:.2f}".format(a))
# print("{:.2f}".format(round(a, 2)))
# print("{:.15f}".format(round(a, 2)))


# for i in range(1,13,1):
#     print(f'{i} {int(i/3) + 1}')
#     # print(math.ceil(i/3))
#
# def filterLucky(mylist):
#     return list(filter(lambda x: '7' in str(x), mylist))
#
# print(filterLucky([1,2,3,4,5,6,7,68,69,70,15,17]))


def trickyDoubles(num: int) -> int:
    d = int(len(str(num)) / 2)
    if str(num)[:d] == str(num)[-d:]:
        return num
    else:
        return num * 2


print(trickyDoubles(7727))


# from sympy import isprime
# def sexy_primes(a, b):
#     if isprime(a) and isprime(b) and abs(a-b) == 6:
#         return True
#     else:
#         return False


def double_check(strng):
    for i in range(len(strng) - 1):
        if strng[i].lower() == strng[i + 1].lower():
            return True
    return False


print(double_check("AabBcC"))


def next_item(xs, item):
    try:
        x = list(xs)
        return x.pop(x.index(item) + 1)
    except:
        return None


print(next_item([1, 2, 3, 4, 5, 6, 7], 3))
print(next_item(["Joe", "Bob", "Sally"], "Bob"))


for num in range(1, 101):
    print(
        "FizzBuzz"
        if (not num % 5 and not num % 3)
        else "Fizz"
        if not num % 3
        else "Buzz"
        if not num % 5
        else str(num)
    )


def next_item(xs, item):
    try:
        x = list(xs)
        return x.pop(x.index(item) + 1)
    except:
        return None


def next_item2(xs, item):
    m = False
    for i in xs:
        if m:
            return i
        if i == item:
            m = True


s = "aabacbaa"
replaced = ""
for i in s:
    replaced += {"a": "b", "b": "a", "c": "c"}[i]
print(replaced)


# [print(['Fizz', '', ''][i % 3] + ['Buzz', '', '', '', ''][i % 5] or i) for i in range(1, 101)]


def create_phone_number(n):
    n = "".join(map(str, n))
    return "(%s) %s-%s" % (n[:3], n[3:6], n[6:])


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

print({True: "1", 1: "one"})

print({1, 1.0, True})
