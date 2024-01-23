#!/usr/bin/python3
"""
This script reads lines from
standard input (stdin) and computes metrics.

It parses each line, extracts relevant information,
and calculates the total file size
along with the count of different HTTP status codes.
Periodically, it displays the metrics.

Usage:
    $ cat log_file.txt | python3 0-stats.py
"""

import sys


def print_metrics(total_size, status_code):
    """
    Function that prints the metrics
    """
    print(f'File size: {total_size}')
    for key, value in sorted(status_code.items()):
        if value != 0:
            print(f'{key}: {value}')


if __name__ == '__main__':
    total_size = 0
    status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        i = 0
        for line in sys.stdin:
            args = line.split()
            if len(args) > 6:
                status = args[-2]
                file_size = args[-1]
                total_size += int(file_size)

                if status in status_code:
                    i += 1
                    status_code[status] += 1

                if i % 10 == 0:
                    print_metrics(total_size, status_code)

    except KeyboardInterrupt:
        print_metrics(total_size, status_code)
        raise
    else:
        print_metrics(total_size, status_code)
