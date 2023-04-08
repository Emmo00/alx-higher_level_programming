#!/usr/bin/python3
"""
text indentation module has one function

text_intention(string)
prints text with 2 new lines after each of these characters:
.
?
:
"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    text_l = list(text)
    for c in text_l:
        print(c, end="")
        if c in [".", "?", ":"]:
            print("\n\n", end="")
