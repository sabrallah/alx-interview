#!/usr/bin/python3

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
    try:
        bytes_data = bytes(data)
        bytes_data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False


if __name__ == "__main__":
    pass
