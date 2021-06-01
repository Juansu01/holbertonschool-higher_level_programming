#!/usr/bin/python3
"""This module defines a function that checks classes """


def is_same_class(obj, a_class):
    """This function returns true or false if
    object is the same type as a_class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
