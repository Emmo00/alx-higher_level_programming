#!/usr/bin/python3
"""Definea add_attribute function
"""


def add_attribute(obj, name, value):
    """adds attribute to an object if possible
    else raise an exception
    """
    if '__dict__' in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
