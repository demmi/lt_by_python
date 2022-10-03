my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[-2])
# for i in my_list[-2]:
#     print(i, end = " ")
# for i in my_list:
#     if type(i)  == list:
#         print(i)
print([x for x in my_list if type(x) == list])


list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
result = list(filter(lambda x: isinstance(x, int), list_1))
print(f'Sum is: {sum(result)}')
letters = list(filter(lambda x: isinstance(x, str), list_1))
for i in letters:
    if 'a' in i:
        print (i)

list1 = ['cat', 'dog', 'horse', 'cow']
tuple1 = tuple(list1)
print (type(tuple1))

names1 = input("Enter your family members, Mr. Johnson:")
names2 = input("Enter your family members, Mr. Baker:")
words1 = names1.split(",")
Johnsons = len(words1)
words2 = names2.split(",")
Bakers = len(words2)
if Johnsons > Bakers:
    print("Johnsons is a bigger family.")
elif Bakers > Johnsons:
    print("Bakers is a bigger family.")
else:
    print("The number of family members is equal.")

film = {
    'title': 'Die',
    'director': 'John Dough',
    'year': '2022',
    'budget': '100.000.000.000',
    'main_actor': "You",
    'slogan': "Die tonight"
}
print(film.keys())
print(film.values())
print(film.items())

my_dictionary = {
    'num1': 375,
    'num2': 567,
    'num3': -37,
    'num4': 21
}
print(sum(my_dictionary.values()))

list1 = [1, 2, 3, 4, 5, 3, 2, 1]
list2 = set(list1)
print(list2)
def unique(list1):
    list2 = []
    unique_numbers = set(list1)
    for number in unique_numbers:
        list2.append(number)
    return list2
print(unique(list1))

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set2.intersection(set1))
print(set2.difference(set1), (set1.difference(set2)))
print(set1.issubset(set2))


