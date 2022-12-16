#!/usr/bin/python3
# handles error
import sys
import urllib.request
import urllib.error


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode())
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
