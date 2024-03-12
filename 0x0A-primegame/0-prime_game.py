#!/usr/bin/python3
"""
0. Prime Game
"""


def is_prime(n):
  """
  This function checks if a number n is prime.
  Replace it with your implementation using trial division or Sieve of Eratosthenes.
  """
  # Implement logic to check for prime numbers
  pass

def remove_multiples(nums, prime):
  """
  This function removes all elements in nums that are multiples of prime.
  """
  new_nums = []
  for num in nums:
    if num % prime != 0:
      new_nums.append(num)
  return new_nums

def play_round(nums, player):
  """
  Simulates a single round of the game.
  """
  primes = [num for num in nums if is_prime(num)]  # Find all primes in nums
  if not primes:
    return "Ben" if player == "Maria" else "Maria"  # Opponent wins if no primes

  # Let the current player choose a prime number (replace with logic for player choice)
  chosen_prime = primes[0]  # Replace with actual player selection

  # Remove the chosen prime and its multiples
  nums = remove_multiples(nums, chosen_prime)

  return "Ben" if player == "Maria" else "Maria"  # Switch player for next round

def isWinner(x, nums):
  """
  Determines the winner of the game after x rounds.
  """
  winner = None
  wins_maria = 0
  wins_ben = 0

  for _ in range(x):
    result = play_round(nums.copy(), "Maria")  # Play a round with Maria starting

    if result != "None":
      winner = result
      break  # Stop if a winner is determined

    # Update nums for next round (consider efficiency here)
    nums = remove_multiples(nums, 2)  # Remove already chosen 2 (optimize this)

    # Switch player for next round
    result = play_round(nums.copy(), "Ben")

    if result != "None":
      winner = result
      break

  if not winner:  # Count wins if no winner after all rounds
    wins_maria = sum(is_prime(num) for num in nums)
    wins_ben = x - wins_maria
    winner = "Maria" if wins_maria > wins_ben else ("Ben" if wins_ben > wins_maria else "None")

  return winner
