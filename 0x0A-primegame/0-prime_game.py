#!/usr/bin/python3
"""
Prime Game module for ALX interview
"""


def is_primme(x):
    """Determine if a number is a prime."""
    if x < 2:
        return False
    for v in range(2, int(x ** 0.5) + 1):
        if x % v == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner."""
    if x < 1 or not nums:
        return None

    maria_win = 0
    ben_win = 0

    max_number = max(nums)
    prime = [is_primme(v) for v in range(max_number + 1)]

    for n in nums[:x]:
        prime_counter = sum(prime[:n])
        if prime_counter % 2 == 0:
            ben_win += 1
        else:
            maria_win += 1

    if maria_win == ben_win:
        return None
    return 'Maria' if maria_win > ben_win else 'Ben'