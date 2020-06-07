#!/usr/bin/python3
"""
Module class.
"""


class MyInt(int):
    """
    class MyInt that inherits from int.
    """
    def __eq__(self, other):
        """
        reversing equality
        """
        return self.__class__.__bases__.__ne__(other)

    def __ne__(self, other):
        """
        reversing inequality
        """
        return self.__class__.__bases__.__eq__(other)
