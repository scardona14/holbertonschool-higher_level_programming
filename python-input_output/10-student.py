#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """__init__ method
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A function that returns dictionary representation of Student"""

        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict