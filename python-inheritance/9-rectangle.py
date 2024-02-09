#!/usr/bin/python3
"""9. Full rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A function that initializes width and height"""

    def __init__(self, width, height):
        """A function that initializes width and height"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """A function that computes area of a rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """A function that returns a string representation of the rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
