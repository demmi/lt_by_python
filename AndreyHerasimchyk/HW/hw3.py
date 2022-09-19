# 3.1
def print_nested_list(lst):
    [print(x) for x in lst if isinstance(x, list)]


my_list = ["a", "b", [1, 2, 3], "d"]
print_nested_list(my_list)


# 3.2
def sum_of_numbers(arr):
    return sum([x for x in list_1 if isinstance(x, int)])


def contains_a(arr):
    return [x for x in list_1 if isinstance(x, str) and "a" in x]


list_1 = ["Hi", "ananas", 2, None, 75, "pizza", 36, 100]
print(sum_of_numbers(list_1))
print(contains_a(list_1))


# 3.3
def convert_to_tuple(lst):
    return tuple(lst)


animals = ["cat", "dog", "horse", "cow"]
print(convert_to_tuple(animals))


# 3.4
def family_comparison(f1, f2):
    family_1_arr = f1.split(",")
    family_2_arr = f2.split(",")
    return (
        "Equal"
        if len(family_1_arr) == len(family_2_arr)
        else family_1_arr
        if len(family_1_arr) > len(family_2_arr)
        else family_2_arr
    )


family_1 = input("Введите членов первой семьи через запятую\n")
family_2 = input("Введите членов второй семьи через запятую\n")
print(family_comparison(family_1, family_2))


# 3.5
def dict_keys(dictionary):
    return [key for key in dictionary.keys()]


def dict_values(dictionary):
    return [value for value in dictionary.values()]


def dict_pairs(dictionary):
    return [pair for pair in dictionary.items()]


film = {
    "title": "House M.D.",
    "director": "David Shore",
    "year": "2004–2012",
    "budget": "unknown",
    "main_actor": "Hugh Laurie",
    "slogan": "Genius has side effects",
}
print(dict_keys(film))
print(dict_values(film))
print(dict_pairs(film))


# 3.6
def sum_of_values(dic):
    return sum([value for value in dic.values()])


my_dictionary = {"num1": 375, "num2": 567, "num3": -37, "num4": 21}
print(sum_of_values(my_dictionary))


# 3.7
def remove_duplicates(lst):
    return list(set(lst))


print(remove_duplicates([1, 2, 3, 4, 5, 3, 2, 1]))


# 3.8
def set_intersection(s1, s2):
    return s1 & s2


def set_difference(s1, s2):
    return s1 ^ s2


def set_issubset(s1, s2):
    return s1 < s2


set1 = {"a", "z", 1, 5, 9, 12, 100, "b"}
set2 = {5, "z", 1, 8, 9, 21, 100, "l", 785}
print(set_intersection(set1, set2))
print(set_difference(set1, set2))
print(set_issubset(set1, set2))
print(set_issubset(set2, set1))
