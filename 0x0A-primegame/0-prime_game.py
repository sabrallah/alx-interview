#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of each round of the prime game.

    :param x: Number of rounds
    :param nums: List of n for each round
    :return: Name of the player that won the most rounds, or None if the winner cannot be determined
    """

    def is_prime(num):
        """Check if a number is prime."""
        # Implementation of prime checking logic (you can use a sieve of Eratosthenes or any other method)

    def get_primes_up_to_n(n):
        """Generate a list of prime numbers up to n."""
        # Implementation of generating prime numbers up to n using the sieve of Eratosthenes

    def remove_multiples(nums, prime):
        """Remove multiples of a prime number from the list."""
        # Implementation of removing multiples of a prime number from the list

    def play_round(nums):
        """Play a round of the prime game and return the winner."""
        # Implementation of playing a round of the prime game and determining the winner

    # Implementation of the main logic to play multiple rounds and determine the overall winner

# Example usage
if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print("Winner: {}".format(isWinner(x, nums)))
