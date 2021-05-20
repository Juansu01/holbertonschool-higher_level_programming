#!/usr/bin/python3
"""
Class defining a square
"""


class Square():

    """ This class assigns size to square and calculates its area """
    def __init__(self, __size=0, position=(0, 0)):
        if not type(__size) is int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        if __size == 0:
            self.__size = __size
        else:
            self.__size = __size
            self.position = position

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

    @property
    def position(self):
        """
        This function retrieves the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        for pos in value:
            if type(pos) is not int or pos < 0 or\
                 len(value) != 2:
                raise TypeError("position must be a\
                     tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        This function prints the square and its spaces based
        off position
        """
        if self.__size != 0:
            if self.__position[1] > 0:
                for newlines in range(self.__position[1]):
                    print("")
            for size in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(" ", end="")
                for hastags in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
# for i in range(self.__size):
#    for j in range(self.__size):
#       print("#", end="")
#  print(""
