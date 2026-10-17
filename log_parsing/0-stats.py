#!/usr/bin/python3
"""Parse HTTP log lines and print cumulative statistics."""

import re
import sys


CODES = (200, 301, 400, 401, 403, 404, 405, 500)
PATTERN = re.compile(
    r'^\S+ - \[[^\]]+\] "GET /projects/260 HTTP/1\.1" '
    r'(\d+) (\d+)$'
)


def print_stats(total_size, counts):
    """Display cumulative file size and status counts."""
    print("File size: {}".format(total_size))
    for code in CODES:
        if counts[code]:
            print("{}: {}".format(code, counts[code]))
    sys.stdout.flush()


def main():
    """Process standard input one line at a time."""
    total_size = 0
    counts = {code: 0 for code in CODES}
    lines = 0

    try:
        for line in sys.stdin:
            lines += 1
            match = PATTERN.fullmatch(line.rstrip("\r\n"))

            if match:
                status = int(match.group(1))
                size = int(match.group(2))
                total_size += size
                if status in counts:
                    counts[status] += 1

            if lines % 10 == 0:
                print_stats(total_size, counts)

    except KeyboardInterrupt:
        print_stats(total_size, counts)
    else:
        if lines % 10 != 0 or lines == 0:
            print_stats(total_size, counts)


if __name__ == "__main__":
    main()
