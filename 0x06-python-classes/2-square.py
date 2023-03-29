#!/usr/bin/python3

"""Define Square class"""


class Square:
    """A square class"""

    def __init__(self, size):
        """__init__: set size
        
        check if size is integer and less than 0

        Args:
            size: size of the square
        Attributes:
            size: private"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
