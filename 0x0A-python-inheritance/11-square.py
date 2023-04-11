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
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def area(self):
        """returns the area of the rectangle
        """
        return self.__width * self.__height
