#!/usr/bin/python3
"""
Write a function that prints a square with the character #.
"""


def print_square(size):
    """
    Write a function that prints a square with the character #.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("{}".format(size*'#'))
