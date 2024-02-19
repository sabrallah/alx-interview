#!/usr/bin/python3
"""Rotate a 2D matrix by 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix by 90 degrees clockwise in-place.

    :param matrix: 2D list representing the matrix to be rotated
    :return: None
    """
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp


# Test the function


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    rotate_2d_matrix(matrix)
    for row in matrix:
        print(row)
