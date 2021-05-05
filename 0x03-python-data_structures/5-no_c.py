#!/usr/bin/env python3


def no_c(my_string):

    nocstring = ""

    for i in my_string:
        if i == "c" or i == "C":
            i = ""
        nocstring += i

    return nocstring
