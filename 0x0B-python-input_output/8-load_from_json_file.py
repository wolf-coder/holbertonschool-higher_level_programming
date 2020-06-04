#!/usr/bin/python3
"""
Module to manage file.
"""
from json import load


def load_from_json_file(filename):
    """
    that creates an Object from a "JSON file"
    """

    with open(filename, 'r') as f:
        return load(f)
