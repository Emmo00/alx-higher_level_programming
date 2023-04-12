#!/usr/bin/python3
json = __import__('json')
"""Defines to_json_string function
"""


def to_json_string(my_obj):
    """returns the JSON representation of
    an object
    """
    return json.dumps(my_obj, sort_keys=True)
