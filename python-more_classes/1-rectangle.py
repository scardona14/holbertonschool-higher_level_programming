#!/usr/bin/python3
""""1. Real definition of a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initializes the instance"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that returns the value of the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """
        Function that sets width instance attribute
        Raise a TypeError & ValueError if not integer of natural number resp.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Method that returns the value of the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """
        Function that sets height instance attribute
        Raise a TypeError & ValueError if not integer of natural number resp.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value
