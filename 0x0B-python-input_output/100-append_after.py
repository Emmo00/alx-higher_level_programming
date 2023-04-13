#!/usr/bin/python3
"""Defines the append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after
    each line containing a specific string
    """
    if filename == "":
        return
    with open(filename, "r", encoding="utf-8") as f:
        text = ""
        line = "go"
        while line:
            line = f.readline()
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
