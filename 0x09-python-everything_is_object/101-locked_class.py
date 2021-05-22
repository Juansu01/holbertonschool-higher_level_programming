#!/usr/bin/python3
""" Class that doesn't allow new instances attributes """


class LockedClass():
    """ Method to avoid the use of different attributes """
    __slots__ = "first_name"
