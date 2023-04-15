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
