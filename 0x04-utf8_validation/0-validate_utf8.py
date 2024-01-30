"""
This module contains a function for validating UTF-8 encoded data.
"""


def validUTF8(data):
    """
    Validate if the given data is UTF-8 encoded.

    Args:
        data (list[int]): The data to be validated.

    Returns:
        bool: True if the data is valid UTF-8 encoded, False otherwise.
    """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) != 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    pass
