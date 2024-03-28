#!/usr/bin/env python3

import sys


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403:
                    0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()
            if len(parts) != 10:
                continue

            status_code = int(parts[8])
            file_size = int(parts[9])

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_size += file_size
            line_count += 1

            if line_count == 10:
                print_stats(total_size, status_codes)
                total_size = 0
                status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403:
                                0, 404: 0, 405: 0, 500: 0}
                line_count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
