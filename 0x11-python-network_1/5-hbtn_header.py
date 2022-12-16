#!/usr/bin/python3
''' gets a header '''
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers['X-Request-Id'])
