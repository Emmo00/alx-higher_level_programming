#!/usr/bin/python3
"""Defines an empty class:
    BaseGeometry
    """


class BaseGeometry():
    """An BaseGeometry class
    """
    def area(self):
        """raises an error if the area
        method is not redefined in a child class or
        instance of this class
        """
        raise Exception("area() is not implemented")
