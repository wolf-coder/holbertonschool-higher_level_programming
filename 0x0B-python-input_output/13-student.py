#!/usr/bin/python3
"""
Module Class
"""


class Student:
    """
    Class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation constructor.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a
        Student instance.
        """
        if type(attrs) is list:
            return {Atr: getattr(self, Atr)
                    for Atr in attrs if Atr in
                    self.__dict__.keys()}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for Key, Val in json.items():
            setattr(self, Key, Val)
