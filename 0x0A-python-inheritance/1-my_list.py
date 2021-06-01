#!/usr/bin/python3
"""This module defines a class that inherits from list """


class MyList(list):
    """This class defines a method that sorts a list."""

    def print_sorted(self):
        """ Don't mind me, just sorting a list and printing it."""
        print(sorted(self))
