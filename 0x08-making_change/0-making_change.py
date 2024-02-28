#!/usr/bin/python3

def makeChange(coins, total):
    # If the total is 0 or less, return 0
    if total <= 0:
        return 0
    
    # Sort the coins in descending order
    coins.sort(reverse=True)
    
    # Initialize a variable to keep track of the number of coins needed
    num_coins = 0
    
    # Iterate through the coins
    for coin in coins:
        # If the coin is greater than the total, continue to the next coin
        if coin > total:
            continue
        
        # Calculate the number of coins needed for the current coin
        num = total // coin
        
        # Update the total to subtract the value of the coins used
        total -= num * coin
        
        # Increment the number of coins used
        num_coins += num
        
        # If the total becomes 0, break out of the loop
        if total == 0:
            break
    
    # If the total is still greater than 0, it means the total cannot be met by the coins given, return -1
    if total > 0:
        return -1
    
    # Return the number of coins needed
    return num_coins
