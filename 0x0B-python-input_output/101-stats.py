#!/usr/bin/python3
''' script for processing requests logs '''
import signal
import re

count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0


def print_logs():
    ''' prints the logs '''
    global status_codes, total_file_size

    print('File size: {:d}'.format(total_file_size))
    for code, tally in status_codes.items():
        if tally:
            print('{:d}: {:d}'.format(code, tally))


def sigint(sig, sframe):
    ''' SIGINT handler '''
    print_logs()
    signal.default_int_handler()


def main():
    ''' logs network requests '''
    global count, status_codes, total_file_size

    signal.signal(signal.SIGINT, sigint)
    r = re.compile(r'(?P<ip_address>.*) - \[(?P<date>.+)\] ".+" ' +
                   r'(?P<status_code>\d+) (?P<file_size>\d+)')
    while True:
        count += 1
        match = r.match(input()).groupdict()
        status_code = int(match['status_code'])
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_file_size += int(match['file_size'])
        if count and not count % 10:
            print_logs()

if __name__ == '__main__':
    main()
