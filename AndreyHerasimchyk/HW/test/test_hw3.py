import unittest

from AndreyHerasimchyk.HW.hw3 import *


class MyTestCase(unittest.TestCase):
    def test_print_nested_list(self):
        self.assertEqual(print_nested_list(["a", "b", [1, 2, 3], "d"]), [[1, 2, 3]])

    def test_sum_of_numbers(self):
        self.assertEqual(sum_of_numbers(["Hi", "ananas", 2, None, 75, "pizza", 36, 100]), 213)

    def test_contain_a(self):
        self.assertEqual(contains_a(["Hi", "ananas", 2, None, 75, "pizza", 36, 100]), ['ananas', 'pizza'])

    def test_convert_to_tuple(self):
        self.assertEqual(convert_to_tuple(["cat", "dog", "horse", "cow"]), ("cat", "dog", "horse", "cow"))

    def test_family_comparison(self):
        self.assertEqual(family_comparison('mom, dad', 'son, daughter'), 'Equal')

    def test_dict_keys(self):
        self.assertEqual(dict_keys({
            "title": "House M.D.",
            "director": "David Shore",
            "year": "2004–2012",
            "budget": "unknown",
            "main_actor": "Hugh Laurie",
            "slogan": "Genius has side effects",
        }), ['title', 'director', 'year', 'budget', 'main_actor', 'slogan'])

    def test_dict_values(self):
        self.assertEqual(dict_values({
            "title": "House M.D.",
            "director": "David Shore",
            "year": "2004–2012",
            "budget": "unknown",
            "main_actor": "Hugh Laurie",
            "slogan": "Genius has side effects",
        }), ['House M.D.', 'David Shore', '2004–2012', 'unknown', 'Hugh Laurie', 'Genius has side effects'])

    def test_dict_pairs(self):
        self.assertEqual(dict_pairs({
            "title": "House M.D.",
            "director": "David Shore",
            "year": "2004–2012",
            "budget": "unknown",
            "main_actor": "Hugh Laurie",
            "slogan": "Genius has side effects",
        }), [('title', 'House M.D.'), ('director', 'David Shore'), ('year', '2004–2012'), ('budget', 'unknown'),
             ('main_actor', 'Hugh Laurie'), ('slogan', 'Genius has side effects')])

    def test_sum_of_values(self):
        self.assertEqual(sum_of_values({"num1": 375, "num2": 567, "num3": -37, "num4": 21}), 926)

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_set_intersection(self):
        self.assertEqual(set_intersection({"a", "z", 1, 5, 9, 12, 100, "b"}, {5, "z", 1, 8, 9, 21, 100, "l", 785}),
                         {1, 100, 5, 9, 'z'})

    def test_set_difference(self):
        self.assertEqual(set_difference({"a", "z", 1, 5, 9, 12, 100, "b"}, {5, "z", 1, 8, 9, 21, 100, "l", 785}),
                         {8, 'l', 12, 785, 21, 'a', 'b'})

    def test_set_issubset(self):
        self.assertFalse(set_issubset({"a", "z", 1, 5, 9, 12, 100, "b"}, {5, "z", 1, 8, 9, 21, 100, "l", 785}))
        self.assertTrue(set_issubset({"z", 1, 5, 9, 100, "l"}, {5, "z", 1, 8, 9, 21, 100, "l", 785}))


if __name__ == '__main__':
    unittest.main()
