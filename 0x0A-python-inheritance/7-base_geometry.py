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

    def integer_validator(self, name, value=None):
        """Validates the value passed to it
        - checks whether it is an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
