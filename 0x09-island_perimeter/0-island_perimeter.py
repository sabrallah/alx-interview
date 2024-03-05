#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of integers): Represents the island grid.

    Returns:
        int: Perimeter of the island.

    Constraints:
        - grid is rectangular, with its width and height not exceeding 100.
        - The grid is completely surrounded by water.
        - There is only one island (or nothing).
        - The island doesn’t have “lakes”
    """
    perimeter = 0

    if not grid or not grid[0]:
        return perimeter

    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter


# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
