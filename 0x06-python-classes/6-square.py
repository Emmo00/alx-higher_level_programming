#!/usr/bin/python3
"""Define Square class"""


class Square:
    """A square class"""

    def __init__(self, size, position=(0, 0)):
        """initialize square, set size.

        Args:
            size (int): size of the square.
            position (tuple): position
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(num, int) for num in position) or not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print("")
            return
        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            for __ in range(self.__size):
                [print("", end="") for _ in range(self.__position[1])]
                print("#", end="")
            print("")
