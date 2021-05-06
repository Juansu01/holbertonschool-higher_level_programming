#!/usr/bin/python3


def uniq_add(my_list=[]):

    list_unique_numbers = []
    unique_numbers = set(my_list)

    for number in unique_numbers:
        list_unique_numbers.append(number)

    return sum(list_unique_numbers)
