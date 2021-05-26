#!/usr/bin/python3
'''
This module defines a function that prints text with two new lines after
these characters: ., ? and :.
'''


def text_indentation(text):
    '''This function prints two new lines after every: ., ? and :. '''
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
