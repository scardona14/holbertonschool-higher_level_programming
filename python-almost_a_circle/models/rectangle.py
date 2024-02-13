#!/usr/bin/python3

"""Rectangle Model"""

from models.base import Base


class Rectangle(Base):
    """A class that defines base initialization of rectangle model"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """A function that defines initialization of instances"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """A function that defines width instance of a rectangle"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """A function that passes the width attribute"""

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """A function that defines height instance of a rectangle"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """A function that passes the height attribute"""

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """A function that defines x attribute of a rectangle"""

        return (self.__x)

    @x.setter
    def x(self, value):
        """A function that passes x attribute"""

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """A function that defines y attribute of a rectangle"""

        return (self.__y)

    @y.setter
    def y(self, value):
        """A function that passes y attribute"""

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """A function that computes the area of a rectangle"""

        return (self.__width * self.__height)

    def display(self):
        """A function that prints a rectangle with "#" character"""

        rectangle = ""
        print_symbol = "#"

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"

        print(rectangle, end="")

    def __str__(self):
        """A function that returns string format of a rectangle"""

        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """A function that assigns key/value argument to attributes"""

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

            return

        try:

            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        except IndexError:
            pass

    def to_dictionary(self):
        """A function that returns the dict representation of a rectangle"""

        return ({'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                 'width': getattr(self, "width")})
