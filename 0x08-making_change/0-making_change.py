#!/usr/bin/python3
"""
this module solve change problem 
"""


def makeChange(coins, total):
    """
    the few number coins need meet the total
    """
    if total <= 0:
        return 0
    coin_min = {0: 0}
    for value in range(1, total + 1):
        coin_min[value] = float('inf')
        for Coin in coins:
            if value >= Coin:
                coin_min[value] = min(coin_min[value],
                                        coin_min[value - Coin] + 1)
    if coin_min[total] != float('inf'):
        return coin_min[total]
    else:
        return -1