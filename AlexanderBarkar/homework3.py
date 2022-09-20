# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
my_list = ['a', 'b', [1, 2, 3], 'd']
print('\nTask 3.1 answer: ' + ', '.join(str(item) for item in my_list[2]))
# -=-=-=-=-=-=-=-
# print('Task 3.1 answer: ', end='')
# print(*my_list[2], sep=', ')
# -=-=-=-=-=-=-=-
# print(f"Task 3.1 answer: {', '.join(map(str, my_list[2]))}")
# если что - в задании вывести не [1, 2, 3], а 1, 2, 3
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(f'\nTask 3.2.1 answer: {sum([l1_item for l1_item in list_1 if str(l1_item).isdigit()])}')
print(f'Task 3.2.2 answer: {[l1_item for l1_item in list_1 if "a" in str(l1_item)]}')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
list2 = ['cat', 'dog', 'horse', 'cow']
print(f'\nTask 3.3 answer: {tuple(list2)}')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('\nTask 3.4:')
family_1 = list(input('Input family 1 members: ').split(','))
family_2 = list(input('Input family 2 members: ').split(','))
print('Answer:')
if len(family_1) > len(family_2):
    print(f'Family 1 is bigger: {family_1}')
elif len(family_2) > len(family_1):
    print(f'Family 2 is bigger: {family_2}')
else:
    print('Equal')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('\nTask 3.5 answers:')
film = {
    'title': 'Достучаться до небес',
    'director': 'Thomas Jahn',
    'year': 1997,
    'budget': 2200000,
    'main_actor': 'Til Schweiger',
    'slogan': 'Быстрый автомобиль, миллион марок в багажнике, и всего одна неделя жить'
    }
print(f'Keys:\t{film.keys()}\nValues:\t{film.values()}\nItems:\t{film.items()}')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(f'\nTask 3.6 answer: {sum(my_dictionary.values())}')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
list_37 = [1, 2, 3, 4, 5, 3, 2, 1]
print(f'\nTask 3.7 answer - final list: {list(set(list_37))}')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print('\nTask 3.8 answers:')
print(f'Значения, которые встречаются в обоих множествах: {set2.intersection(set1)}')
print(f'Значения set2, которые не встречаются в set1: {set2.difference(set1)}')
print(f'Значения set1, которые не встречаются в set2: {set1.difference(set2)}')
print('Множество set1 является подмножеством set2? Ответ: ' + ('ДА' if set1.issubset(set2) else 'НЕТ'))
print('Множество set2 является подмножеством set1? Ответ: ' + ('ДА' if set2.issubset(set1) else 'НЕТ'))
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
