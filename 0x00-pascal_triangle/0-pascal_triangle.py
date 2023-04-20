#!/usr/bin/python3
"""0-pascal_traingle.

Creating a pascal triangle for a given number n.
"""


def factorial(x):
    """Return the factorial of the input.

    The complexity should fit the requirement.
    """
    if x < 1:
        return 1
    else:
        return (x * factorial(x - 1))


def pascal_triangle(n):
    """
    Return a list of integers representing.

    the Pascal's triangle of n.
    """
    triangle = [[]]
    if n <= 0:
        return []
    for i in range(n):
        if i < n - 1:
            triangle.append([])
        for j in range(i + 1):
            triangle[i].append(int(
                factorial(i)/(factorial(i - j) * factorial(j))))
    return triangle
