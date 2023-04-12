#!/usr/bin/python3
"""Defines from_json_string function
"""


json = __import__('json')


def from_json_string(my_str):
    """returns the python object representation of
    a string
    """
    return json.loads(my_str)
