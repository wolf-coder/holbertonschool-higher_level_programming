#!/usr/bin/python3
"""
Module to manage file.
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text
    file, using a JSON representation.
    """

    with open(filename, 'w') as f:
        dump(my_obj, f)
