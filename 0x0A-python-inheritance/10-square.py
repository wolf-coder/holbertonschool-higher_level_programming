#!/usr/bin/python3
"""
Module class that inherits from Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Module Square ingerits form Rectangle
    """
    def __init__(self, size):
        """
        initialisation of attributes
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
