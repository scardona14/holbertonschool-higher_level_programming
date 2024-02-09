#!/usr/bin/python3
"""7. Integer validator"""


class BaseGeometry:
    """"An empty class BaseGeometry."""

    def area(self):
        """Function that computes area (not implemented yet)"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A function that validates name & value
        Raises TypeError & ValueError if not int or positive resp.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
