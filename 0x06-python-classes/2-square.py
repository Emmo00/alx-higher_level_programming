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
