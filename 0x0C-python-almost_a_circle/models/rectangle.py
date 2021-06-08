#!/usr/bin/python3
""" This module defines a class Rectangle. """
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """This initializes the width, hegiht, x, y and id of the
        rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ This is the width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """ This is the width setter."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ This is the height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """ This is the height setter."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ This is the x getter."""
        return self.__x

    @x.setter
    def x(self, value):
        """ This is the x setter."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ This is the x getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """ This is the y setter."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    """Public methods."""

    def area(self):
        """This public method returns the area
        of a triangle."""
        return self.__width * self.__height
