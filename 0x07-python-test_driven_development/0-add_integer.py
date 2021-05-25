#!/usr/bin/python3
'''
This module defines a function that returns the sum of two integers.
'''


def add_integer(a, b=98):
    ''' The function adds a and b, then returns the result '''
    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    if not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
