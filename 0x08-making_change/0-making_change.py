#!/usr/bin/python3
"""
Making Change problem

https://www.algoexpert.io/questions/Making%20Change

Given an infinite number of quarters (25 cents), dimes (10 cents),
nickels (5 cents), and pennies (1 cent), write code to calculate the
number of ways of making n cents.

Constraints:
0 <= n <= 10000

Example:
n = 4

Number of ways of making 4 cents is 4. The ways are:
1 cent, 1 cent, 1 cent, 1 cent
1 cent, 1 cent, 2 pennies
1 cent, 2 nickels
2 pennies, 2 pennies

Assumptions:
- Coins have infinite supply

Algorithm:
Dynamic programming

Time Complexity:
O(n)

Space Complexity:
O(n)

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



