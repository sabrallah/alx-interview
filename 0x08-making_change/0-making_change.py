#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize table with max value for each amount
    table = [float("inf")] * (total + 1)
    table[0] = 0  # 0 coins needed for 0 total
    
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                # Recurrence relation 
                table[i] = min(table[i], table[i - coin] + 1)

    return table[total] if table[total] != float("inf") else -1
