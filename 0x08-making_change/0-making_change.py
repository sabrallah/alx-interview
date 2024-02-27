#!/usr/bin/python3

""" Containe MakeChange function"""


def makeChange(coins, total):
    """
    Returns: few numbers coins need to meet totals
        If totals is 0 or less, return 0
        If totals cannot be mets by number coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coind in coins:
        while coind <= total:
            total -= coind
            change += 1
        if (total == 0):
            return change
    return -1
