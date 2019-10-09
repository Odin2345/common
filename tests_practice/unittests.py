import unittest
from homework import (
    without_duplicates_list,
    number_letter_a_in_str,
    power_of_three,
    result_single_digit,
    zeros_to_the_end,
    arithmetic_progression,
    number_not_occur_twice,
    missing_list_number,
    count_elements_until_tuple,
    string_reversed_order)


class TaskTestCases(unittest.TestCase):

    def test_without_duplicates_list(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(without_duplicates_list(a, b), [1, 2, 3, 5, 8, 13])

    def test_number_letter_a_in_str(self):
        self.assertEqual(number_letter_a_in_str(
            "I am a good developer. I am also a writer", "a"), 5)

    def test_power_of_three(self):
        self.assertEqual(power_of_three(9), True)
        self.assertEqual(power_of_three(12), False)

    def test_result_single_digit(self):
        self.assertEqual(result_single_digit(59), 5)

    def test_zeros_to_the_end(self):
        self.assertEqual(zeros_to_the_end([0, 2, 3, 4, 6, 7, 10]),
                         [2, 3, 4, 6, 7, 10, 0])

    def test_arithmetic_progression(self):
        self.assertEqual(arithmetic_progression([5, 7, 9, 11]), True)
        self.assertEqual(arithmetic_progression([5, 8, 9, 11]), False)
        self.assertEqual(arithmetic_progression([5, 10, 15, 20, 24]), False)

    def test_number_not_occur_twice(self):
        self.assertEqual(number_not_occur_twice([5, 3, 4, 3, 4]), 5)

    def test_missing_list_number(self):
        self.assertEqual(missing_list_number([1, 2, 3, 4, 6, 7, 8]), 5)

    def test_count_elements_until_tuple(self):
        self.assertEqual(count_elements_until_tuple([1, 2, 3, (1, 2), 3]), 3)

    def test_string_reversed_order(self):
        self.assertEqual(string_reversed_order("Hello World and Coders"),
                         "sredoC dna dlroW olleH")


if __name__ == "__main__":
    unittest.main()
