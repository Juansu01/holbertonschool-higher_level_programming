#!/usr/bin/python3
"""
Class defining a square
"""


class Square():
    __size = None
    area = None
    """ This class defines a size and area for Square """
    def __init__(self, __size=0):
        if not type(__size) is int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        if __size == 0:
            self.__size = __size
        else:
            self.__size = __size
