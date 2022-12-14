#!/usr/bin/python3
# checks error
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.post(url)
    if res.status_code >= 400:
        print('Error code:', res.status_code)
    else:
        print(res.text)
