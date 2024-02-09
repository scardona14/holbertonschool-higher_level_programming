#!/usr/bin/python3
"""10. Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle."""

    def __init__(self, size):
        """A function that initializes size"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
