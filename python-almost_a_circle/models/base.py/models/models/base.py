#!/usr/bin/python3

"""Base Model"""

import csv
import json
import turtle


class Base:
    """A class that defines the base for all models present"""

    __nb_objects = 0

    def __init__(self, id=None):
        """A function that initializes a new base instance"""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function that returns JSON representation of a list of dicts"""

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """A function that Writes JSON serialization of objects to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")

            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """A function that returns the deserialization of a JSON string"""

        if json_string is None or json_string == "[]":
            return ([])

        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """A function that returns a class instantied from a dictionary"""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)

            else:
                new = cls(1)

            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """A function that returns a list of classes instantiated from JSON"""

        filename = str(cls.__name__) + ".json"
        try:

            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return ([cls.create(**d) for d in list_dicts])

        except IOError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A function that writes the CSV serialization of objects to a file"""

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")

            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]

                else:
                    fieldnames = ["id", "size", "x", "y"]

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """A function that returns a list of classes from a CSV file"""

        filename = cls.__name__ + ".csv"
        try:

            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]

                else:
                    fieldnames = ["id", "size", "x", "y"]

                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return ([cls.create(**d) for d in list_dicts])

        except IOError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A function that draws Rectangles & Squares using turtle module."""

        t = turtle.Turtle()
        t.screen.bgcolor("#000000")
        t.pensize(3)
        t.shape("turtle")

        t.color("#FFFFFF")
        for rect in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()

            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("#FFFF00")
        for sq in list_squares:
            t.showturtle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()

            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()