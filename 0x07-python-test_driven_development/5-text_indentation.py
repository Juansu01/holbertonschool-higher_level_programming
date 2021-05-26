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
        print("{}".format(i), end="")
        if i == ".":
            print("")
            print("")
        if i == ":":
            print("")
            print("")
        if i == "?":
            print("")
            print("")
