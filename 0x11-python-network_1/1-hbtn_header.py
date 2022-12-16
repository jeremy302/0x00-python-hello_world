#!/usr/bin/python3
''' gets header '''
import sys
import urllib.request

if __name__ == '__main__':
    if sys.argv[1:]:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as res:
            print(res.headers['X-Request-Id'])
