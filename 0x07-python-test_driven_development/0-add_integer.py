#!/usr/bin/python3



def add_integer(a, b=98):
    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    if not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
