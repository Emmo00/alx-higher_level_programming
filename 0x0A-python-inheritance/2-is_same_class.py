#!/usr/bin/python3
"""defines `is_same_class`
Example:
    >>> a = 20
    >>> is_same_class(a, int)
    True
    """


def is_same_class(obj, a_class):
    """returns True if obj is exactly an instance of
    a_class
    else False
    """
    return obj.__class__ == a_class
