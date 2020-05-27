#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """
    A class Square that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        init initialization method
        args:
        size (int): Parameter indicating size of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        """
        if isinstance(value, tuple)\
           and len(value) == 2 and isinstance(value[0], int)\
           and isinstance(value[1], int) and value[0] * value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        """
        if self.size:
            for y in range(self.position[1]):
                print()
            for Y in range(self.size):
                for x in range(self.position[0]):
                    print(' ', end='')
                for X in range(self.size):
                    print("#", end='')
                print()
            
        else:
            print()
