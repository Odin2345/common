import math


def without_duplicates_list(a, b):
    return list(set(a) & set(b))


def number_letter_a_in_str(a_str, letter):
    return a_str.count(letter)


def power_of_three(number):
    return math.log(number, 3) == int(math.log(number, 3))


def result_single_digit(number):
    while len(str(number)) > 1:
        sum_number = 0
        for i in list(str(number)):
            sum_number += int(i)
        number = sum_number
    return number


def zeros_to_the_end(new_list):
    return [i for i in new_list if i != 0] + [i for i in new_list if i == 0]


def arithmetic_progression(list_progr):
    for i in range(3, len(list_progr), 1):
        if list_progr[i] - list_progr[i-1] != list_progr[1] - list_progr[0]:
            return False
    return True


def number_not_occur_twice(list_number):
    for i in list_number:
        if list_number.count(i) == 1:
            return i


def missing_list_number(list_number):
    new_list_number = [i for i in range(1, len(list_number) + 2)]
    return list(set(new_list_number) ^ set(list_number))[0]


def count_elements_until_tuple(list_number):
    counter = 0
    for i in list_number:
        if isinstance(i, tuple):
            return counter
        else:
            counter += 1


def string_reversed_order(some_line):
    return some_line[::-1]


def number_hours_and_minutes(some_int_number):
    return str(some_int_number // 60) + ':' + str(some_int_number % 60)


def largest_word_in_string(some_line):
    return max(some_line.split())


def string_in_backwards_order(input_func):
    some_text = input_func()
    return " ".join([i for i in some_text.split()[::-1]])


def output_fib_numbers_to_generate(input_func):
    number_fib = input_func()
    num1 = 1
    num2 = 1
    count = 0
    fib_numbers = []
    while count < number_fib:
        fib_numbers.append(num1)
        tmp = num1 + num2
        num1 = num2
        num2 = tmp
        count += 1
    return fib_numbers


def new_list_even_elements(some_list):
    return [i for i in some_list if i % 2 == 0]


def sum_input_number(input_func):
    num = int(input_func())
    return sum(range(num + 1))


def return_factorial_number(some_number):
    fact_number = 1
    for i in range(1, some_number + 1):
        fact_number *= i
    return fact_number


def alphabetical_shift_letters_in_line(some_text):
    vowels = "aeiou"
    return "".join([chr(ord(i) + 1).upper() if chr(ord(i) + 1) in vowels
                    else chr(ord(i) + 1) for i in some_text])


def letters_row_in_alphabetical_order(some_text):
    return "".join(sorted(some_text))


def comparison_of_two_numbers(first_number, second_number):
    if first_number == second_number:
        return "-1"
    else:
        return first_number < second_number
