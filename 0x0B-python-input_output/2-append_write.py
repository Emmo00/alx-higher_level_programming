#!/usr/bin/python3
"""Defines the append_write function
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file and returns the
    number of characters added
    """
    if filename == "":
        return 0
    with open(filename, "a", encoding="utf-8") as file:
        return(file.write(text))
