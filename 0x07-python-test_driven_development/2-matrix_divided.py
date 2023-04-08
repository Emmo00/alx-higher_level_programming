#!/usr/bin/python3
"""
This is the add_integer module

The add_integer module supplies one function, add_integer(). For example,
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    result = [[(x / div) for x in row] for row in matrix]
    return result