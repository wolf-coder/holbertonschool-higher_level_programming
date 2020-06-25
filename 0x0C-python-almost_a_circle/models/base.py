#!/usr/bin/python3
"""
Module
"""


class Base:
    """Documentation for Base

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
