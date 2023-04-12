#!/usr/bin/python3
"""Defines the write_file function
"""


def write_file(filename="", text=""):
    """writes string to a text file and returns the number
    of characters writted
    """
    if filename == "":
        return 0
    with open(filename, "w", encoding="utf-8") as file:
        return(file.write(text))
