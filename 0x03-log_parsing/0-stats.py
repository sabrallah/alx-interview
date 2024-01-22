#!/usr/bin/python3

import sys


def print_statistics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))


def process_line(line, total_size, status_counts):
    parts = line.split()
    if len(parts) == 10 and parts[8].isdigit():
        status_code = int(parts[8])
        file_size = int(parts[9])

        total_size += file_size

        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

        return total_size, status_counts

    return total_size, status_counts


def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            total_size, status_counts = process_line(line,
                                                     total_size, status_counts)

            if i % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        pass

    # Print final statistics before exiting
    print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
