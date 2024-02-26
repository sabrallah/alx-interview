#!/usr/bin/python3
def makeChange(coins, total):
    """
    Function to determine the fewest number of coins needed to meet a given amount total.
    
    Parameters:
    coins (list): A list of the values of the coins in your possession
    total (int): The total amount to meet

    Returns:
    num_coins (int): The fewest number of coins needed to meet total. Returns -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total == 0:
            return num_coins
        num_coins += total // coin
        total %= coin
    if total != 0:
        return -1
    return num_coins
