#!/usr/bin/python3
"""
Module to read file
"""


def read_file(filename=""):
    """
    """
    with open(filename, "r") as f:
        print(f.read())
