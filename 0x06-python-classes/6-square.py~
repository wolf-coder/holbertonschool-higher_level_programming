#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """
    A class Square that defines a square
    """
    def __init__(self, size=0):
        """
        init initialization method
        args:
        size (int): Parameter indicating size of the square.
        """
        self.size = size

    def area(self):
        """
        area Calculate the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        """
        if isinstance(size, int):
            if size < 0:
                raise TypeError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise ValueError("size must be an integer")

    def my_print(self):
        """
        """
        if self.size:
            for i in range(self.size):
                for j in range(self.size):
                    print("{}".format("#"), end='')
                print()
        else:
            print()
