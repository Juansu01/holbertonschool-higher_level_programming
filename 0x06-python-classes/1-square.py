#!/usr/bin/python3
"""
Class defining a square
"""


class Square():
    __size = None
    """ This class defines a private size for a Square """

    def __init__(self, __size=None):
        if __size is not None:
            self.__size = __size
