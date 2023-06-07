#!/usr/bin/python3
"""Rotate 2D Matrix."""


def swap(matrix, a, b, c, d):
    """Swap the two values."""
    temp = matrix[a][b]
    matrix[a][b] = matrix[c][d]
    matrix[c][d] = temp


def rotate_2d_matrix(matrix):
    """Rotate matrix 90 degrees clockwise."""
    length = len(matrix)
    maxim = length - 1
    for i in range(length):
        for j in range(i + 1, length):
            swap(matrix, i, j, j, i)
    for row in matrix:
        row.reverse()
