#!/usr/bin/python3
""" This module defines the function write_file. """


def write_file(filename="", text=""):
    """ This function opens a file and writes text to it. """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
