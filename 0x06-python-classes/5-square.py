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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if value == 0:
            self.__size = value
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
