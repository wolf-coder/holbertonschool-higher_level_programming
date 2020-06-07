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
        return super().__class__.__ne__(int(self), other)

    def __ne__(self, other):
        """
        reversing inequality
        """
        return super().__class__.__eq__(int(self), other)
