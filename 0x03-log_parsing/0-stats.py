#!/usr/bin/env python3
"""
Module for calculating statistics of input data
"""

import sys


def print_stats(numbers):
    """
    Prints the minimum, maximum, sum, and average of a list of numbers
    """
    if len(numbers) == 0:
        print("No numbers provided")
        return

    min_num = min(numbers)
    max_num = max(numbers)
    sum_num = sum(numbers)
    avg_num = sum_num / len(numbers)

    print(f"Minimum: {min_num}")
    print(f"Maximum: {max_num}")
    print(f"Sum: {sum_num}")
    print(f"Average: {avg_num}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-stats.py [list of numbers]")
        sys.exit(1)

    numbers = []
    for arg in sys.argv[1:]:
        try:
            numbers.append(int(arg))
        except ValueError:
            print(f"Invalid number: {arg}")
            sys.exit(1)
    
        print_stats(numbers)
