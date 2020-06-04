#!/usr/bin/python3
"""
Module to manage file.
"""
from json import dumps


def to_json_string(my_obj):
    """
    unction that returns the JSON representation of an object (string).
    """
    return dumps(my_obj)
