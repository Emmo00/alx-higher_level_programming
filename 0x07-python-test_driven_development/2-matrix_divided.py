#!/usr/bin/python3
"""
This is the add_integer module

The add_integer module supplies one function, add_integer(). For example,
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    length = len(matrix[0])
    for row in matrix:
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    result = [[round(x / div, 2) for x in row] for row in matrix]
    return result
