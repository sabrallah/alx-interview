#!/usr/bin/python3
"""
This module contains the minOperations function
"""


def minOperations(n):
    """
    Calculate the minimum operations to achieve exactly n H characters

    :param n: int
    :return: int
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    ops = 0
    h = 2

    while h <= n:
        # Check if n is divisible by current h
        while n % h == 0:
            ops += h
            n //= h
        h += 1

    return ops
