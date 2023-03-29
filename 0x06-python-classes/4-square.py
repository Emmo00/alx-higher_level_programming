#!/usr/bin/python3
"""Define Square class"""


class Square:
    """A square class"""

    def __init__(self, size):
        """initialize square, set size.

        Args:
            size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of square

        Args:
            no arguments
        Return:
            area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
