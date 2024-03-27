#!/usr/bin/python3
"""
Log stats module
"""
import sys
from operator import itemgetter


def log_parser(log):
    """
    Parses log into different fields
    """
    log_fields = log.split()
    file_size = int(log_fields[-1])
    status_code = log_fields[-2]
    return status_code, file_size


def validate_format(log):
    """
    Validates log format
    """
    return False if len(log.split()) < 7 else True


def validate_status_code(status_code):
    """
    Check if status code entry is valid
    """
    valid_status_codes = ["200", "301", "400", "401",
                          "403", "404", "405", "500"]
    return True if status_code in valid_status_codes else False


def print_log(file_size, status_codes) -> None:
    """
    Prints out log files
    """
    sorted_status_codes = sorted(status_codes.items(), key=itemgetter(0))
    print('File size: {}'.format(file_size))
    for code_count in sorted_status_codes:
        key = code_count[0]
        value = code_count[1]
        print("{}: {}".format(key, value))


def main():
    """
    Reads logs from std in and prints out statistic
    on status code and file size
    """
    status_codes_count = {}
    total_size = 0
    log_count = 0
    try:
        for log in sys.stdin:
            log_count += 1
            if not validate_format(log):
                continue
            status_code, file_size = log_parser(log)
            total_size += file_size
            if validate_status_code(status_code):
                entry = {status_code:
                         status_codes_count.get(status_code, 0) + 1}
                status_codes_count.update(entry)
            if not log_count % 10:
                print_log(total_size, status_codes_count)
    except KeyboardInterrupt:
        print_log(total_size, status_codes_count)
    print_log(total_size, status_codes_count)


if __name__ == '__main__':
    main()