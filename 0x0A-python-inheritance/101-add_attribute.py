#!/usr/bin/python3
"""
Module
"""


def add_attribute(obj, attr, value):
    """
    attributes setter.
    """
    if "__dict__" in dir(obj):
        setattr(obj, attr, value)
    else:
        raise Exception("can't add new attribute")
