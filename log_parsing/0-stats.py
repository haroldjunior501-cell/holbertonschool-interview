#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print accumulated file size and status code counts."""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {:d}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) > 2 and parts[-2].isdigit() and parts[-1].isdigit():
                status = parts[-2]
                total_size += int(parts[-1])
                if status in status_counts:
                    status_counts[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
    print_stats(total_size, status_counts)
