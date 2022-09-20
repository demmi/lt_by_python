import os
import math


# def user_friendly_size(file_size):
#     sizes = {40: 'TB', 30: 'GB', 20: 'MB', 10: 'kB', 0: 'B'}
#     if isinstance(file_size, str):
#         file_size = os.stat(file_size).st_size
#     for power, symbol in sizes.items():
#         if file_size // 2 ** power:
#             return f'{file_size / 2 ** power:.2f} {symbol}'

def user_friendly_size(file_size) -> str:
    symbols = ('B', 'kB', 'MB', 'GB', 'TB')
    if isinstance(file_size, str):  # Если аргумент - строка
        if file_size.isdigit():  # Если протупили и отправили число строкой
            file_size = int(file_size)
        else:
            file_size = os.stat(file_size).st_size  # Получим размер файла в байтах
    sym_index = int(math.log(file_size, 2) // 10)
    return f'{file_size / 2 ** (sym_index * 10):.2f} {symbols[sym_index]}'


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
        level += {'F': 0, 'U': 1, 'D': -1}[path]
        if level == 0 and path == 'U':
            valley += 1
    return valley
