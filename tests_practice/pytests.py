import pytest

from homework import (
    number_hours_and_minutes,
    largest_word_in_string,
    string_in_backwards_order,
    output_fib_numbers_to_generate,
    new_list_even_elements,
    sum_input_number,
    return_factorial_number,
    alphabetical_shift_letters_in_line,
    letters_row_in_alphabetical_order,
    comparison_of_two_numbers)


def test_number_hours_and_minutes():
    number_input = 63
    assert number_hours_and_minutes(number_input) == "1:3"


def test_largest_word_in_string():
    assert largest_word_in_string("fun&!! time") == "time"
    assert largest_word_in_string("I love dogs") == "love"


def test_string_in_backwards_order():
    assert string_in_backwards_order(lambda: "My name is Michele") \
           == "Michele is name My"


def test_output_fib_numbers_to_generate():
    assert output_fib_numbers_to_generate(lambda: 7) == [1, 1, 2, 3, 5, 8, 13]


def test_new_list_even_elements():
    numbers_input = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert new_list_even_elements(numbers_input) == [4, 16, 36, 64, 100]


def test_sum_input_number():
    assert sum_input_number(lambda: 4) == 10


def test_return_factorial_number():
    assert return_factorial_number(4) == 24


def test_alphabetical_shift_letters_in_line():
    assert alphabetical_shift_letters_in_line("abcd") == "bcdE"


def test_letters_row_in_alphabetical_order():
    assert letters_row_in_alphabetical_order("edcba") == "abcde"


def test_comparison_of_two_numbers():
    num1 = 10
    num2 = 15
    assert comparison_of_two_numbers(num1, num2) is True
    assert comparison_of_two_numbers(num2, num1) is False
    assert comparison_of_two_numbers(num1, num1) == "-1"
