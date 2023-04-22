#!/usr/bin/python3
"""0-pascal_traingle.

Creating a pascal triangle for a given number n.
"""


def pascal_triangle(n):
    """
    Return a list of integers representing.

    the Pascal's triangle of n.
    """
    triangle = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        line = [1]
        for j in range(len(triangle[i - 1]) - 1):
            line.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        line.append(1)
        triangle.append(line)
    return triangle
