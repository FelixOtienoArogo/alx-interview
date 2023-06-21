#!/usr/bin/python3
"""Island perimeter."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid."""
    perimeter = 0

    if type(grid) != list:
        return perimeter
    for i, row in enumerate(grid):
        max = len(row)
        for j, element in enumerate(row):
            if (j + 1 < max):
                if(element == 1):
                    perimeter += 4
                    if(row[j + 1] == 1):
                        perimeter -= 1
                    if(row[j - 1] == 1):
                        perimeter -= 1
                    if(grid[i - 1][j] == 1):
                        perimeter -= 1
                    if(grid[i + 1][j] == 1):
                        perimeter -= 1
    return perimeter
