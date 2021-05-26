#!/usr/bin/python3
'''
This module defines a function that prints text with two new lines after
these characters: ., ? and :.
'''


def text_indentation(text):
    '''This function prints two new lines after every: ., ? and :. '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == ".":
            print("{}\n".format(i))
        elif i == ":":
            print("{}\n".format(i))
        elif i == "?":
            print("{}\n".format(i))
        else:
            print(i, end="")


