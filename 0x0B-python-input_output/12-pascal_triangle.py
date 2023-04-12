#!/usr/bin/python3
"""Define pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n:
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        t = [1] * (i + 1)
        for j in range(i + 1):
            if j + 1 == len(t) or j == 0:
                continue
            t[j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
        triangle.append(t)
    return triangle
