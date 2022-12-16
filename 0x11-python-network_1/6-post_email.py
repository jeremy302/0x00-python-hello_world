#!/usr/bin/python3
# performs POST request
import sys
import requests


if __name__ == '__main__':
    url, email = sys.argv[1:3]
    res = requests.post(url, params={'email': email})
    print(res.text)
