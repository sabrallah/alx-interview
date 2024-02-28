#!/usr/bin/python3
"""
This module contains the solution to the "Change comes from within" project
"""

def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    using coins in the list of values

    Args:
        coins (list): List of coin values
        total (int): Total amount to make with coins

    Returns:
        int: Fewest number of coins needed to meet total
            or -1 if total cannot be made with coins
    """
    coins = sorted(coins, reverse=True)
    count = 0
    for coin in coins:
        while total - coin >= 0:
            count += 1
            total -= coin
    return count if total == 0 else -1

