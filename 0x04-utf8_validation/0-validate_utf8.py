#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): List of integers representing 1 byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    # Number of trailing bytes for the current UTF-8 character
    num_trailing_bytes = 0

    for num in data:
        # Check if the current byte is a trailing byte
        if num_trailing_bytes == 0:
            if (num >> 7) == 0b0:
                # Single byte character
                continue
            elif (num >> 5) == 0b110:
                # Two byte character
                num_trailing_bytes = 1
            elif (num >> 4) == 0b1110:
                # Three byte character
                num_trailing_bytes = 2
            elif (num >> 3) == 0b11110:
                # Four byte character
                num_trailing_bytes = 3
            else:
                # Invalid start of UTF-8 character
                return False
        else:
            # Check if the current byte is a trailing byte
            if (num >> 6) == 0b10:
                num_trailing_bytes -= 1
            else:
                # Invalid trailing byte
                return False

    # Check if there are missing trailing bytes at the end
    return num_trailing_bytes == 0

# Test cases


if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105,
             115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
