#!/usr/bin/python3
"""Defines the read_file function
"""


def read_file(filename=""):
    """Reads content of a file and prints it
    to stdout
    """
    if filename == "":
        return
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
