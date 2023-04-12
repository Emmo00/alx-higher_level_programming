#!/usr/bin/python3
"""Defines save_to_json_file function
"""


json = __import__('json')


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a
    JSON representation:
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f, sort_keys=True)
