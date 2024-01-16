#!/usr/bin/python3
"""
0-minoperations.py - Minimum Operations
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to obtain exactly n 'H' characters.

    :param n: The target number of 'H' characters.
    :return: The minimum number of operations or 0 if impossible.
    """
    if n <= 1:
        return n

    # Initialize variables
    operations = 0
    clipboard = 1
    current = 1

    while current < n:
        if n % current == 0:
            clipboard = current
            operations += 1
        current += clipboard

    return operations
