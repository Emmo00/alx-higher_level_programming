#!/usr/bin/python3
"""Defines to_json_string function
"""
json = __import__('json')



def to_json_string(my_obj):
    """returns the JSON representation of
    an object
    """
    return json.dumps(my_obj, sort_keys=True)
