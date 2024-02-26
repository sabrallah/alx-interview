#!/usr/bin/python3
"""
0. Change comes from within
Given a pile of coins of different values, determine the fewest number of coins needed
to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list
Your solutions runtime will be evaluated in this task
"""

def makeChange(coins, total):
    if total < 0:
        return 0
    if total == 0:
        return 0
    
    # Initialize an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

# Sample test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
