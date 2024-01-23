#!/usr/bin/python3

import sys

def print_statistics(total_size, status_count):
    print(f"File size: {total_size}")
    for code in sorted(status_count):
        print(f"{code}: {status_count[code]}")

def parse_line(line, total_size, status_count):
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += size

        if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
            status_count[status_code] = status_count.get(status_code, 0) + 1

        return total_size, status_count

    except (ValueError, IndexError):
        return total_size, status_count

def main():
    total_size = 0
    status_count = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size, status_count = parse_line(line.strip(), total_size, status_count)

            if i % 10 == 0:
                print_statistics(total_size, status_count)

    except KeyboardInterrupt:
        pass  # Handle keyboard interruption

if __name__ == "__main__":
    main()
