#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        try:
            if len(parts) >= 7:
                status = int(parts[-2])
                size = int(parts[-1])
                total_size += size
                if status in status_counts:
                    status_counts[status] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
        except (ValueError, IndexError):
            pass
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
