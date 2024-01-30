#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        - data: list of integers representing 1 byte of data
    Returns:
        - True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # If the current byte is the start of a new character
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if byte >> 7 == 0b0:
                num_bytes = 1
            elif byte >> 5 == 0b110:
                num_bytes = 2
            elif byte >> 4 == 0b1110:
                num_bytes = 3
            elif byte >> 3 == 0b11110:
                num_bytes = 4
            else:
                return False
        else:
            # Check if the current byte is a continuation byte
            if byte >> 6 != 0b10:
                return False

            # Decrement the number of bytes expected for the current character
            num_bytes -= 1

    # If there are remaining bytes to complete a character, it's invalid
    return num_bytes == 0
