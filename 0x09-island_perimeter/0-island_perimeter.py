#!/usr/bin/python3
"""Island perimeter."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid."""
    perimeter = 0

    if type(grid) != list:
        return perimeter
    glen = len(grid)
    for i, row in enumerate(grid):
        rlen = len(row)
        for j, element in enumerate(row):
            if element == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == rlen - 1 or (rlen > j + 1 and row[j + 1] == 0),
                i == glen - 1 or (len(grid[i + 1]) > j and
                                  grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
                    )
            perimeter += sum(edges)
    return perimeter
