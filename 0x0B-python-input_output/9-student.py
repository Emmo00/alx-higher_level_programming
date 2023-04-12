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

    def to_json(self):
        """returns a dictionary representation of a
        Student instance
        """
        return self.__dict__
