#!/usr/bin/python3
"""Defines a Square class
that inherits from Rectangle class
    """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A  square class
    """
    def __init__(self, size):
        """instantiate class object
        sets private attributes: size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the rectangle
        """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(
                self.__size,
                self.__size)
