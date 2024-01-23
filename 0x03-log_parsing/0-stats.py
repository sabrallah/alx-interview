#!/usr/bin/python3
import sys
import signal

# Initialize variables
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0


def print_stats():
    print("File size: {:d}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:s}: {:d}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Handle Ctrl+C


signal.signal(signal.SIGINT, signal_handler)


# Main loop
if __name__ == "__main__":
    for i, line in enumerate(sys.stdin, 1):
        try:
            parts = line.split()
            status_code = parts[-2]
            file_size += int(parts[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except IndexError:
            pass
        if i % 10 == 0:
            print_stats()

    print_stats()
