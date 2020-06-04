#!/usr/bin/python3
"""
Module to manage file.
"""


def number_of_lines(filename=""):
    """
    function that returns the number of lines of
    a text file.
    """
    n = 0
    with open(filename, "r") as f:
        for line in f:
            n += 1
    return n
