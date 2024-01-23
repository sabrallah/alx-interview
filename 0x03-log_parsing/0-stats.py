#!/usr/bin/python3
import sys

"""
This script parses log lines from stdin, calculates the total file size, and counts the occurrences of each status code.
"""

def print_stats(total_size, status_codes):
    """
    Print the total file size and the count of each status code.

    Args:
        total_size (int): The total size of the file.
        status_codes (dict): A dictionary containing the count of each status code.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    """
    Parse a log line and extract the size and status code.

    Args:
        line (str): The log line to parse.

    Returns:
        tuple: A tuple containing the size and status code extracted from the log line.
    """
    try:
        parts = line.split()
        size = int(parts[-1])
        code = int(parts[-2])
        return size, code
    except (IndexError, ValueError):
        return None, None

def main():
    """
    Main function that reads log lines from stdin, parses them, and prints the statistics.

    Returns:
        None
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            size, code = parse_line(line)
            if size is not None and code is not None:
                total_size += size
                if code in status_codes:
                    status_codes[code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
