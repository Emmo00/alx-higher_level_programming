#!/usr/bin/python3
"""Defines the Base class
"""

class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialise base class
        """
        if id != None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def validate_integer(self, name, value=None):
        """validate integers passed, raises an
        exception if not an interger
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and name in ['x', 'y']:
            raise ValueError("{} must be >= 0".format(name))
        if value <= 0 and name not in ['x', 'y']:
            raise ValueError("{} must be > 0".format(name))
