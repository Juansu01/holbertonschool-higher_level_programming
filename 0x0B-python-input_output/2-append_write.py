#!/usr/bin/python3
""" This module defines the function append_write. """


def append_write(filename="", text=""):
    """ This function opens filename and appends text to it. """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
