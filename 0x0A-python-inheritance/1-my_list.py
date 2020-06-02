#!/usr/bin/python3
"""
(module Info)
"""


class MyList(list):
    """
    Mylist class inherated from list
    """
    def print_sorted(self):
        """
        sorting a list
        """
        print(sorted(self))
