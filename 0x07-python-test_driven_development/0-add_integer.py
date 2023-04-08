#!/usr/bin/python3
"""
This is the add_integer module

The add_integer module supplies one function, add_integer(). For example,

>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """Returns the addition of two integers"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
