#!/usr/bin/python3
"""
This module contains a function that determines the fewest number of coins
needed to meet a given amount total.

The function uses dynamic programming to solve the problem. It first creates
a list `dp` where `dp[i]` is the fewest number of coins needed to make `i`
amount of change. It initializes `dp[i]` to infinity for all `i`, except
`dp[0]` which is 0 because no coins are needed to make 0 amount of change.

Then it iterates over each coin, and for each coin, it updates `dp[x]` for
all `x` from `coin` to `total`. The new value of `dp[x]` is the minimum of
the current value of `dp[x]` and `dp[x - coin] + 1`. The `+1` represents
using one coin of denomination `coin` to make `x` amount of change.

Finally, it returns `dp[total]` if it's not infinity, otherwise it returns -1
indicating that the total cannot be met by any number of coins.
"""


def make_change(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list): A list of integers representing the values of the coins in your possession.
    total (int): The total amount to meet.

    Returns:
    int: The fewest number of coins needed to meet total. If total is 0 or less, return 0.
    If total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0
    dp = [float("inf")] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[total] if dp[total] != float("inf") else -1
