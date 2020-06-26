#!/usr/bin/python3
"""
Module doc
"""
from models.base import Base


class Rectangle(Base):
    """
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        """
        return self.width * self.height

    def display(self):
        """
        """
        print("{}".format("\n"*self.y), end="")
        for i in range(self.height):
            print("{}{}".format(' '*self.x, "#"*self.width), end="\n")

    def __str__(self):
        """
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        """
        """
        if args:
            attr = dict([(0, "id"), (1, "width"), (2, "height"),
                         (3, "x"), (4, "y")])
            for i, v in enumerate(args):
                setattr(self, attr[i], v)
        for k, v in kwargs.items():
            setattr(self, k, v)
