#!/usr/bin/python3
"""Defines a rectangle class
that inherits from BaseGeometry class
    """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A  rectangle class
    """
    def __init__(self, width, height):
        """instantiate class object
        sets private attributes: width, height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
