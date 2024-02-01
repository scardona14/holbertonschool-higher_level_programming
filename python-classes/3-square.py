#!/usr/bin/python3
"""
3. Area of a square
A class Square that defines a square by: (based on 2-square.py)
"""

class Square:
    """" A class that defines a square by size"""

    def __init__(self, size=0):
        """"
        Define private instance attribute: size
        Raise TypeError & ValueError if not int or <0 resp"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

        def area(self):
            """"Function that calculates area"""

            return (self.__size ** 2)