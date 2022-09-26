# # Структуры данных. Списки, кортежи, словари и множества: lists, tuples, dictionaries, sets
# # ----------------------- LISTS -----------------------
# # ----- Create a list: option 1
# lst = []  # [] - квадратные скобки означают список
# print(lst)
#
# # ----- Create a list: option 2
# lst = [1, 'string', 12.3, 'Hello', 25]
# print(lst)
#
# # ----- Create a list: option 3
# sentence = 'What a wonderful life!'
# my_list = list(sentence)  # переменная sentence - аргумент для функции list
# print(my_list)  # по умолчанию выводит отдельно каждый символ в кавычках: ['W', 'h', ...]
# --- Если нужен другой разделитель, то:
# phrase = 'What a wonderful life!'
# my_list1 = phrase.split(' ')  # в методе split пробел указан в качестве разделителя
# print(my_list1)  # выводит отдельно то, что разделено пробелом
# ---
# phrase = 'What a wonderful life!'
# my_list1 = phrase.split(' ')
# print(my_list1[-1])  # Выведем из списка последний индекс [-1]: слово life!
# print(my_list1[0])  # Выведем первый [0]: слово What
# --- Если требуется извлечь срез – часть списка:
# print(my_list1[-3:-1])  # Выведем индексы в диапазоне [-3:-1]: ['a', 'wonderful']
# print(my_list1[-2:])  # Вывод двух последних: ['wonderful', 'life!']
# print(my_list1[0:2])  # Вывод двух первых: ['What', 'a']
# print(my_list1[:])  # Вывод всего списка, как и print(my_list1)
#
# # For loop with list
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num*2)
#
# l1 = [8, 7, 5, 10]
# print(max(l1))  # max item: 10
# print(min(l1))  # min item: 5

# --- Сравнение списков
#
# l1 = [8, 7, 5, 10]
# l2 = [1, 2, 3, 4, 555]
# l3 = [9, 2]
#
# print(l1 > l2)  # True - списки сравниваются поэлементно
# print(l1 > l3)  # False
#
# print(l1 + l2)  # [8, 7, 5, 10, 1, 2]
#
# # ----- In-place list mutating
#
# l = [8, 7, 5, 10]
# print(l)  # [8, 7, 5, 10]
#
# print(id(l))  # id списка
# l[0] = 0.2  # Заменим первый [0] элемент в списке на 0.2
# print((l))  # [0.2, 7, 5, 10]
# print(id(l))  # id списка при этом не меняется
# --- Метод .append - добавим к l другой список l1:
# l = [8, 7, 5, 10]
# print(l)  # [8, 7, 5, 10]
# print(id(l))
# l1 = [25, 80]
# l.append(l1)
# print(l)  # [8, 7, 5, 10, [25, 80]] второй список по умолчанию добавляется в конец первого
# print(id(l))  # id списка при этом не меняется, это тот же список!
# print(l[-1])  # вложенный список воспринимается, как один последний элемент: [25, 80]
# print(l[-1][0])   # 25 - первый элемент во вложенном списке
#
# # --- Методы .append and .extend()
# l = [8, 7, 5, 10]
# l1 = [25, 80]
# add = 'extra'
# l.append(add)
# l1.extend(add)
# print(l)  # [8, 7, 5, 10, 'extra'] append добавляет переменную add, как один элемент
# print(l1)  # [25, 80, 'e', 'x', 't', 'r', 'a'] extend продлевает список элементами переменной add
#
# # --- Методы .sort() and sorted()
#
# nums = [2, 3, 1, 5, 6, 4, 0]
# print(f'Initial list: {nums}')
# print(id(nums))
# #
# print('--- SORTED()')
# print(f'New sorted list: {sorted(nums)}')  # sorted создает новый сортированный список
# print(f'Initial list after sorting: {nums}')  # исходный список при этом не меняется
# print(id(sorted(nums)))
# #
# print('--- .SORT()')
# print(f'New sorted list: {nums.sort()}')  # None: sort не создает новый сортированный список
# print(f'Initial list After sorting: {nums}')  # sort сортирует исходный список nums
# print(id(nums))
# print(nums.reverse())  # реверс элементов списка
# print(nums)
# print(id(nums))
# #
# lst = ['b', 'c', 'a', 'd']
# print(lst)  # ['b', 'c', 'a', 'd']
# lst1 = sorted(lst)
# print(lst1)  # ['a', 'b', 'c', 'd']
# lll = [3, 1, 5, 2, 6, 4]
# lll.sort()
# print(lll)  # [1, 2, 3, 4, 5, 6]
# lll.reverse()
# print(lll)  # [6, 5, 4, 3, 2, 1]
# - Метод sorted можно применять и для строки:
# str1 = 'da2bec1'
# print(sorted(str1))  # получим список ['1', '2', 'a', 'b', 'c', 'd', 'e']
# print(sorted(str1, reverse=True))  # список в обратном порядке ['e', 'd', 'c', 'b', 'a', '2', '1']
#
# # --- Slicing (Нарезка)
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(letters[0:-1:2])  # со 1го по последний, НЕ включая последний, с шагом 2:  ['a', 'c', 'e']
# print(letters[-3])  # третий с конца: d
# print(letters[::-1])  # реверс с шагом 1: ['f', 'e', 'd', 'c', 'b', 'a']
# print(letters[1:-1])  # со второго по последний, НЕ включая последний: ['b', 'c', 'd', 'e']
# print(letters[::-2])  # реверс с шагом 2: ['f', 'd', 'b']
# print(letters[2:])  # с третьего до конца: ['c', 'd', 'e', 'f']
#
# # --- Метод list comprehension (дословно, понимание или осмысление списка)
# #
# l = [1, 2, 3, 4, 5]
# new_l = []
# for x in l:  # для переменной x в списке l
#     if x % 2:  # если x нечетное (или то же самое if x % 2 != 0:)
#         new_l.append(x * x)  # формируем новый список из элементов, равных x * x
# print(new_l)  # [1, 9, 25]
# # --- То же самое, более кратким синтаксисом:
# new_l = [x * x for x in l if x % 2]  # список из x * x для x из списка l, если x нечетное
# print(new_l)  # [1, 9, 25]
# # - если хотим для четных чисел, то меняем условие так:
# new_l = [x * x for x in l if x % 2 == 0]
# print(new_l)
#
# # ----------------------- TUPLES -----------------------
#
# # ----- Create a tuple: option 1
mytuple = 1, 2, 3  # кортеж пишется через запятую
print(mytuple)  # (1, 2, 3) - кортеж выводится в круглых скобках
#
# # ----- Create a tuple: option 2
# my_tuple = (1, True, 'name', None, 'name', 'name', 25)  # можно в круглых скобках
# print(my_tuple)  # (1, True, 'name', None, 'name', 'name', 25)
#
# name = 'Mark',  # поставив запятую, превращаем переменную в кортеж
# print(name)  # ('Mark',)
#
# name = ('Mark',)
# print(name)  # ('Mark',)
# print(type(name))  # <class 'tuple'>
#
# name = ('Mark')  # без запятой круглые скобки не превращают в кортеж
# print(name)  # Mark
# print(type(name))  # <class 'str'>
#
# --- Распаковка
# letters = ('apple', 'banana', 'cat')
# a, b, c = letters  # все равно, что: a, b, c = 'apple', 'banana', 'cat'
# print(a)  # apple
# print(b)  # banana
# print(c)  # cat
# print(a, b, c)  # apple banana cat
#
# letters[0] = 'ananas'   # изменение элементов в кортеже невозможно: name 'letters' is not defined
# print(letters)
#
# letters = list(letters)  # функция list делает кортеж списком
# letters[0] = 'ananas'  # тогда в списке letters можно изменить элемент
# print(letters)  # список letters: ['ananas', 'banana', 'cat']
# print(tuple(letters))  # сконвертировали список в новый кортеж: ('ananas', 'banana', 'cat')
#
# # ----- Getting index of items
# my_tuple = (1, True, 'name', None, 'name', 'name',25)
# print(my_tuple.index('name'))  # 2 - индекс первого по порядку 'name'
# print(my_tuple.count('name'))  # 3 - 'name' встречается 3 раза
#
# # ----- Filtering (Фильтрация)
# my_tuple = (1, True, 'name', None, 'name', 'name',25)
# result = tuple(filter(lambda x: isinstance(x, int), my_tuple))  # isinstance(x, int) - x экземпляр класса int
# result1 = tuple(filter(lambda x: isinstance(x, str), my_tuple))
# print(result)  # отфильтрованы целые числа: (1, True, 25)
# print(result1)  # отфильтрованы строчные данные: ('name', 'name', 'name')
#
# # --- Tuple methods
# my_tuple = (1, True, 'name', None, 'name', 'name', 25)
# result = tuple(filter(lambda x: isinstance(x, int), my_tuple))
# print(result)
# print(f'Sum is: {sum(result)}')  # Сумма целых чисел: Sum is: 27
# print(f'Max is: {max(result)}')  # Max is: 25
# print(f'Min is: {min(result)}')  # Min is: 1
# print(f'Length of my_tuple is: {len(my_tuple)}')  # Длина (количество элементов): Length of my_tuple is: 7
# print(f'Length of result is: {len(result)}')  # Длина отфильтрованного результата: Length of result is: 3
#
# # ----- Iterate tuple with for loop ( то же для list и для str)
# my_tuple = (1, True, 'name', None, 'name', 'name', 25)
# for (index, item) in enumerate(my_tuple):  # enumerate - перечислить index для каждого item
#     print(index, '-', item, end='; ')  # 0 - 1; 1 - True; 2 - name; 3 - None; 4 - name; 5 - name; 6 - 25;
#
# # ----- iterate tuple with while loop
# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])  # вывод каждого элемента, пока i < длины кортежа
#     i += 1
#
# # ----- Nested list in tuple (Вложенный список в кортеже)
# letters = ('apple', ['ananas', 'mango'], 'melon')
# letters[1][0] = 'cherry'  # во 2м элементе кортежа [списке] меняем 1й элемент 'ananas'
# print(letters)  # ('apple', ['cherry', 'mango'], 'melon')
#
# # ----- swaping variables (Обмен переменных)
# a = 5
# b = 10
# a, b = b, a
# print(f'a = {a}')  # a = 10
# print(f'b = {b}')  # b = 5
#
# # Passing tuple as an argument in function (Передача кортежа, как аргумента, в функцию)
# def sum_it(*args):  # * - означает, что кортеж args (аргумент) распаковывается
#     total = 0
#     for num in args:
#         total = total + num
#     return total
#
#
# print(sum_it(4, 5, 10, 6, 20))  # выводится сумма всех элементов: 45
#
# def func(*args):    # приходит произвольное количество аргументов
#     l = []          # сохраняем их в новый список
#     for item in args:  # и каждый из аргументов
#         l.append(item*item)  # возводим в квадрат
#     return l
#
#
# print(func(2, 5, 6, 8, 10))  # получили список с новыми значениями: [4, 25, 36, 64, 100]
# --- ! Кортеж работает быстрее и занимает меньше памяти, чем список
#
# # -------------------- DICTIONARIES --------------------
# my_dict = {
#     'name': 'Anna',  # пара - уникальный ключ : значение
#     'last_name': 'Pavlova',
#     'age': 30,
#     'department': 'IT'
# }
#
# print(my_dict)  # {'name': 'Anna', 'last_name': 'Pavlova', 'age': 30, 'department': 'IT'}
# print(id(my_dict))
# print(my_dict['name'])  # Anna
# my_dict['last_name'] = 'Smirnova'  # значение ключа 'last_name' меняем на 'Smirnova'
# print(my_dict)  # {'name': 'Anna', 'last_name': 'Smirnova', 'age': 30, 'department': 'IT'}
# print(id(my_dict))
# print(len(my_dict))  # длина словаря: 4 пары ключ-значение
# my_dict['salary'] = 5000  # добавили зарплату - новую пару 'salary': 5000
# print(my_dict)  # {'name': 'Anna', 'last_name': 'Smirnova', 'age': 30, 'department': 'IT', 'salary': 5000}
# print(my_dict.keys())  # получаем ключи: dict_keys(['name', 'last_name', 'age', 'department'])
# print(my_dict.values())  # получаем значения: dict_values(['Anna', 'Pavlova', 30, 'IT'])
# print(my_dict.items())  # dict_items([('name', 'Anna'), ('last_name', 'Pavlova'), ('age', 30), ('department', 'IT')])
# print(my_dict.pop('salary'))  # удалить ключ: 'salary'
# print(my_dict)  # {'name': 'Anna', 'last_name': 'Pavlova', 'age': 30, 'department': 'IT'}
# print(my_dict.get('salary', 'Not found'))  # метод .get - получить значение ключа 'salary', если не найдено: Not found
# print(my_dict.get('name', 'Not found'))  # по ключу 'name' найдено значение: Anna
#
#
# # -------------------- SETS (Множества)  --------------------
# print(set([1, 8, 2, 1, 5, 8, 9]))  # удаляются не уникальные ключи {1, 2, 5, 8, 9}
#
# set1 = {1, 2, 3, 'one', 'ten'}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}
#
# --- Сравнение множеств
# print(set1.issubset(set2))  # set1 есть подмножество set2: True
# print(set2.issuperset(set1))  # set2 включает в себя подмножество set1: True
# print(set2.intersection(set1, set3))  # set2 пересекается с множествами set1, set3: {1, 2, 3}
# print(set2.difference(set1))  # set2 отличается от set1: {100, 525}
#
# --- Удаление и добавление элементов
# print(set1)  # {1, 2, 3, 'ten', 'one'}
# print(set1.remove('one'))  # методом .remove удаляем из множества 'one', на экран не выводится: None
# print(set1)  # удалили 'one': {1, 2, 3, 'ten'}
# print(set1.add(8))  # методом .add добавляем 8, на экран не выводится: None
# print(set1)  # добавили 8: {1, 2, 3, 8, 'ten'}
#
# --- Защита множества от изменений - заморозка
# fs = frozenset({1, 2, 3})
# print(fs)  # frozenset({1, 2, 3})
# если попробуем .remove или .add, получим ошибку атрибута:
# fs.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'
# print(fs)  # множество не изменилось: frozenset({1, 2, 3})
#
# fs.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'
# print(fs)  # множество не изменилось: frozenset({1, 2, 3})
#
#
