#!/usr/bin/python3
"""
Module to manage file.
"""


def to_json_string(my_obj):
    from json import dumps
    """
    unction that returns the JSON representation of an object (string).
    """
    return dumps(my_obj)
