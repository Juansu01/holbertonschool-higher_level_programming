#!/usr/bin/python3


def search_replace(my_list, search, replace):

    if not my_list:
        return []
    else:
        copy = my_list[:]
        for i in range(0, len(copy)):
            if copy[i] == search:
                copy[i] = replace
        return copy
