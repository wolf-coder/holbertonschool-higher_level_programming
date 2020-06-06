#!/usr/bin/python3
"""
Module class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """
        Rectangle sublass of BaseGeometry
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """
        Method returning the area of the Rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        str constructor
        """
        return "[{}] {}/{}".format("Rectangle",
                                   self.__width, self.__height)
