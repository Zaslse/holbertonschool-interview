#!/usr/bin/python3
"""Parse HTTP logs and print cumulative statistics."""

import re
import sys


CODES = (200, 301, 400, 401, 403, 404, 405, 500)

PATTERN = re.compile(
    r'^\S+ - \[[^\]]+\] "GET /projects/260 HTTP/1\.1" '
    r'(\S+) (\d+)$'
)


def print_stats(total_size, counts):
    """Print file size and status code statistics."""
    print("File size: {}".format(total_size))
    for code in CODES:
        if counts[code]:
            print("{}: {}".format(code, counts[code]))
    sys.stdout.flush()


def main():
    """Process log lines from standard input."""
    total_size = 0
    counts = {code: 0 for code in CODES}
    lines = 0

    try:
        for line in sys.stdin:
            lines += 1
            match = PATTERN.match(line.rstrip("\r\n"))

            if match:
                status_text = match.group(1)
                total_size += int(match.group(2))

                if status_text.isdigit():
                    status = int(status_text)
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
