#!/usr/bin/python3
'''
This module defines a function that prints text with two new lines after
these characters: ., ? and :.
'''


def text_indentation(text):
    '''This function prints two new lines after every: ., ? and :. '''
    flag = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == ".":
            flag = 1
            print("{}\n".format(i))
        elif i == ":":
            flag = 1
            print("{}\n".format(i))
        elif i == "?":
            flag = 1
            print("{}\n".format(i))
        else:
            if flag == 1:
                flag = 0
                continue
            print(i, end="")
