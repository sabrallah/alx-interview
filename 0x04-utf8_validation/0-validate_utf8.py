#!/usr/bin/python3
"""
Main file for testing
"""


def validUTF8(data):
    """
    Method to determine if a given data set represents a valid UTF-8 encoding
    """
    # Helper function to check if a byte is a valid start byte
    def is_start_byte(byte):
        return bin(byte).startswith('0b1' + '0' * max(6 - len(bin(byte)), 0))

    # Helper function to check if a byte is a valid continuation byte
    def is_continuation_byte(byte):
        return bin(byte).startswith('0b10')

    # Initialize count to track expected continuation bytes
    count = 0

    # Iterate through each byte in the data
    for byte in data:
        if count == 0:
            # Check for the number of bytes in the character
            if byte < 0b10000000:
                continue
            elif byte < 0b11000000:
                return False
            elif byte < 0b11100000:
                count = 1
            elif byte < 0b11110000:
                count = 2
            elif byte < 0b11111000:
                count = 3
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not is_continuation_byte(byte):
                return False
            count -= 1

    # Check if there are any remaining expected continuation bytes
    return count == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # Should print True

    data = [80, 121, 116, 104, 111, 110, 32, 105,
            115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # Should print True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # Should print False
