#!/usr/bin/python3
"""8. Compare rectangles"""


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
        """Function that computes area of a rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Function that computes perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """
        Function that defines instance method to print rectangle with #
        Raise exception to print rectangle with given characters
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = ""

        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)

                except Exception:
                    rectangle += type(self).print_symbol

            if column < self.__height - 1:
                rectangle += "\n"

        return (rectangle)

    def __repr__(self):
        """Function that defines instance method to return rectangle with #"""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Function that defines instance method to delete rectangle"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Function that defines comparison of area instance attribute
        Raise TypeError if rectangle area value is not integer
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
