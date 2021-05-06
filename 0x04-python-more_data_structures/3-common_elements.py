#!/usr/bin/python3


def common_elements(set_1, set_2):

    list_as_set = set(set_1)
    intersection = list_as_set.intersection(set_2)

    return intersection