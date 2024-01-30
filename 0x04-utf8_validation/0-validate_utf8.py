import sys

def validUTF8(data):
    num_trailing_bytes = 0

    for num in data:
        if num_trailing_bytes == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                num_trailing_bytes = 1
            elif (num >> 4) == 0b1110:
                num_trailing_bytes = 2
            elif (num >> 3) == 0b11110:
                num_trailing_bytes = 3
            else:
                return False
        else:
            if (num >> 6) == 0b10:
                num_trailing_bytes -= 1
            else:
                return False

    return num_trailing_bytes == 0


if __name__ == "__main__":
    data = sys.argv[1:]
    data = [int(num) for num in data]
    result = validUTF8(data)
    print(result)
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
