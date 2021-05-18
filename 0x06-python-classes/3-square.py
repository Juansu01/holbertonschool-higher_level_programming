#!/usr/bin/python3
"""
Class defining a square
"""


class Square():

    """ This class assigns size to square and calculates its area """
    def __init__(self, __size=0):
        if not type(__size) is int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        if __size == 0:
            self.__size = __size
        else:
            self.__size = __size

    def area(self):
        """
        This function calculates the square area
        Returns: The square area
        """
        return self.__size * self.__size
