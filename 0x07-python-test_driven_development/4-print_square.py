#!/usr/bin/python3
"""
print_square module hase one function:

print_square()
Example:
    >>> print_square(4)
    ####
    ####
    ####
    ####
"""


def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
        return
    for _ in range(size):
        for __ in range(size):
            print("#", end="")
        print("")
