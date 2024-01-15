#!/usr/bin/python3
"""
0-minoperations.py - Contains the minOperations function to calculate
the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters.

    Parameters:
    - n (int): The target number of H characters.

    Returns:
    - int: The minimum number of operations needed.
    """
    if n <= 1:
        return n

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return minOperations(n // i) + i

    return n
