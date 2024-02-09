#!/usr/bin/python3
"""11. Square #2"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle."""

    def __init__(self, size):
        """A function that initializes size"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """A function that computes area of a square"""

        return self.__size * self.__size
    
    def __str__(self):
        """A function that returns a string representation of the square"""

        return "[Square] {}/{}".format(self.__size, self.__size)
