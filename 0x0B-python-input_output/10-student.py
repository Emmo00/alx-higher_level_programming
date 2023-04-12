#!/usr/bin/python3
"""Defines the Student class
"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """initializes the Student class
        object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a
        Student instance
        """
        if type(attrs) == list:
            mdict = {}
            for attr in attrs:
                if type(attr) != str:
                    return self.__dict__
                if attr in self.__dict__.keys():
                    mdict[attr] = self.__dict__[attr]
            return mdict
        else:
            return self.__dict__
