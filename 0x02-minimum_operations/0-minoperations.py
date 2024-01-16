def minOperations(n):
    """
    Calculates the minimum number of operations needed to reach n H characters.

    Args:
        n: The target number of H characters.

    Returns:
        The minimum number of operations, or 0 if n is impossible to achieve.
    """

    if n < 1:
        return 0  # Invalid input

    operations = 0
    while n > 1:
        # Find the largest power of 2 that divides n
        largest_power = 0
        while n % 2 == 0:
            n //= 2
            largest_power += 1

        # Add the number of operations for this power
        operations += largest_power
        n -= largest_power  # Subtract remaining characters after division

    # Add one final operation to copy the remaining character
    return operations + 1
