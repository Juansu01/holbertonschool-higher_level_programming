#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    copy = dict(a_dictionary)
    for key in copy:
        copy[key] *= 2
    return copy
