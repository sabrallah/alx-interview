#!/usr/bin/python3
"""
Making Change problem
"""


def makeChange(coins, total):
    """
    Return number of ways to make change

    Args:
        coins (List[int]): Coins
        total (int): Total

    Returns:
        int: Number of ways to make change
    """
    ways = [0] * (total + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, total + 1):
            ways[i] += ways[i - coin]

    return ways[total]



