#!/usr/bin/python3
"""
0-pascal_traingle.

Creating a pascal triangle for a given number n.
"""
import math


def pascal_triangle(n):
    """Return a list of integers representing the Pascal's triangle of n."""
    triangle = [[]]
    if n <= 0:
        return triangle
    for i in range(n):
        if i < n - 1:
            triangle.append([])
        for j in range(i + 1):
            triangle[i].append(int(
                math.factorial(i)/(math.factorial(i - j) * math.factorial(j))))
    return triangle
