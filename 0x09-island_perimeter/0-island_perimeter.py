#!/usr/bin/python3
"""
This module defines a function island_perimeter that calculates the perimeter
of an island represented in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of ints): The grid representation of the map,
                                     where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output should be 12
