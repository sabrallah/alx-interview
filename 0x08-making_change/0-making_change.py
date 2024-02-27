#!/usr/bin/python3
"""
This module solves the change problem
"""


def make_change(coins, total):
    """
    Finds the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    coin_min = {0: 0}
    for value in range(1, total + 1):
        coin_min[value] = float('inf')
        for coin in coins:
            if value >= coin:
                coin_min[value] = min(coin_min[value], coin_min[value - coin] + 1)
    if coin_min[total] != float('inf'):
        return coin_min[total]
    else:
        return -1
