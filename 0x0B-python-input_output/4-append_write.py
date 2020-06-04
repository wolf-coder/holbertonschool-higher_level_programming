#!/usr/bin/python3
"""
Module to manage file.
"""


def append_write(filename="", text=""):
    """
    function that appends a string.
    """

    with open(filename, "a") as f:
        return f.write(text)
