#!/usr/bin/python3
''' script for processing requests logs '''
import signal
import re
import sys

count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0


def print_logs():
    ''' prints the logs '''
    global status_codes, total_file_size

    print('File size: {:d}'.format(total_file_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code]:
            print('{:d}: {:d}'.format(status_code, status_codes[status_code]))


def sigint(sig, sframe):
    ''' SIGINT handler '''
    if count % 10:
        print_logs()
    signal.default_int_handler()
    exit(1)


def main():
    ''' logs network requests '''
    global count, status_codes, total_file_size

    # signal.signal(signal.SIGINT, sigint)
    r = re.compile(r'(?P<ip_address>.*) - \[(?P<date>.+)\] ' +
                   r'"GET /projects/260 HTTP/1.1" ' +
                   r'(?P<status_code>\d+) (?P<file_size>\d+)\w*$')
    while True:
        count += 1
        try:
            inp = input()
            match = r.match(inp).groupdict()
            spl = inp.split(' ')
            if not match:
                continue
        except EOFError:
            print_logs()
            exit()
        except KeyboardInterrupt as er:
            print_logs()
            raise er
        status_code = int(spl[-2])  # int(match['status_code'])
        # if status_code in status_codes:
        status_codes[status_code] += 1
        total_file_size += int(spl[-1])  # int(match['file_size'])
        if not count % 10:
            print_logs()

if __name__ == '__main__':
    main()
