#!/usr/bin/python3
"""3. String representation"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Function that initializes instances for width & height"""

        self.height = height
        self.width = width

    @property
    def height(self):
        """Function that retrieves height instance attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """
        function that sets height instance attribute
        Raise TypeError and ValueError if not integer or natural number resp.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """Function that retrieves width instance attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """
        Function that sets width instance attribute
        Raise TypeError & ValueError if not integer or natural number resp.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def area(self):
        """Function that computes area of a rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Function that computes perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """Function that defines instance method to print rectangle with #"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = ""

        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"

            if column < self.__height - 1:
                rectangle += "\n"

        return (rectangle)
