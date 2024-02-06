#!/usr/bin/python3
"""7. Change representation"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Method that initializes the instance"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Method that returns the rectangle area"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Method that returns the rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Method that returns the string representation of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""

        return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Method that returns the string representation of the rectangle"""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Method that deletes an instance of Rectangle"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1