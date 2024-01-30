#!/usr/bin/env python
"""
This module provides a function to validate UTF-8 encoded data.
"""


def validUTF8(data):
    """
    Validates whether the given data is UTF-8 encoded.

    Args:
        data (list[int]): The data to be validated.

    Returns:
        bool: True if the data is valid UTF-8 encoded, False otherwise.
    """
    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
