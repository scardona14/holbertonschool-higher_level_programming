#!/usr/bin/python3
"""9. A square is a rectangle"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Function that initializes instances for width & height"""

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """Function that returns the rectangle's area"""

        return self.__width * self.__height

    def perimeter(self):
        """Function that returns the rectangle's perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """Function that prints the rectangle with the character #"""

        if self.__width == 0 or self.__height == 0:
            return ""

        return (str(self.print_symbol) * self.__width + "\n") * self.__height

    def __repr__(self):
        """Function that returns a string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Function that prints a message when an instance is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect):
        """Function that compares two rectangles and returns the bigger one"""

        if isinstance(rect_1, Rectangle) and isinstance(rect, Rectangle):
            return rect_1 if rect_1.area() >= rect.area() else rect
        else:
            raise TypeError("rect_1 and rect must be instances of the Rectangle class")
