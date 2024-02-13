#!/usr/bin/python3

"""Square Model"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a Square model"""

    def __init__(self, size, x=0, y=0, id=None):
        """A function that initializes square instances"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """A function that defines size attribute of a square model"""

        return (self.width)

    @size.setter
    def size(self, value):
        """A function that passes size attribute of a square model"""

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """A function that assigns key/value argument to square attributes"""

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

            return

        try:

            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        except IndexError:
            pass

    def __str__(self):
        """A function that returns string format of a square representation"""

        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__,
                self.id, self.x, self.y, self.width))

    def to_dictionary(self):
        """A function that returns dictionary representation of a Square"""

        return ({'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                 'x': getattr(self, "x"), 'y': getattr(self, "y")})
