#!/usr/bin/python3

"""
An empty class Rectangle
"""


class Rectangle:
    """
    Empty class Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        """
        if (self.__height * self.__width) is 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        """
        print("->", Rectangle.print_symbol)
        if (self.__height * self.__width) is 0:
            return ""
        else:
            Str = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    Str += str(self.print_symbol)
                if i < self.__height - 1:
                    Str += "\n"
            return Str

    def __repr__(self):
        """
        """
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        """
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
