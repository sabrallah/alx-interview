#!/usr/bin/python3
"""
0. Prime Game
"""

def isWinner(x, nums):
    """
    Determines the winner of each round of the prime game.

    Parameters:
        x (int): Number of rounds
        nums (list): Array of n for each round

    Returns:
        str or None: Name of the player that won the most rounds, or None if the winner cannot be determined
    """

    def is_prime(num):
        """
        Checks if a number is prime.

        Parameters:
            num (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Generates a list of prime numbers up to n.

        Parameters:
            n (int): Upper limit

        Returns:
            list: List of prime numbers up to n
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def count_moves(nums, primes):
        """
        Counts the number of moves each player can make.

        Parameters:
            nums (int): Number for the current round
            primes (list): List of prime numbers up to nums

        Returns:
            dict: Dictionary with counts for each player's moves
        """
        count = {'Maria': 0, 'Ben': 0}
        for prime in primes:
            if prime > nums:
                break
            count['Maria' if nums % (prime + 1) == 0 else 'Ben'] += 1
        return count

    winners = {'Maria': 0, 'Ben': 0}

    for n in nums:
        primes = get_primes(n)
        moves = count_moves(n, primes)

        # Determine the winner of the round
        if moves['Maria'] == moves['Ben']:
            # If the moves are equal, no winner for the round
            continue
        winners['Maria' if moves['Maria'] > moves['Ben'] else 'Ben'] += 1

    # Determine the overall winner
    if winners['Maria'] == winners['Ben']:
        return None
    return 'Maria' if winners['Maria'] > winners['Ben'] else 'Ben'
