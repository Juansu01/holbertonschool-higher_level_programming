#!/usr/bin/python3
""" This module defines the function read_file. """


def read_file(filename=""):
    """ This function reads a file and prints its content. """
    with open(filename, encoding='utf-8') as f:
        lines = f.read()
    print(lines, end="")
