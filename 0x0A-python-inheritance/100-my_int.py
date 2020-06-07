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
        return super().__ne__(other)

    def __ne__(self, other):
        """
        reversing inequality
        """
        return super().__eq__(other)
