#!/usr/bin/python3
"""
Module class
"""


class BaseGeometry:
    """
    Improving Geometry class
    """
    def area(self):
        """
        Public instance method:raises an
        Exception with the message area()
        is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        value Validation :must ba a strictly positive intger.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
