#!/usr/bin/python3
''' performs POST request '''
import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url, email = sys.argv[1:3]
    data = urllib.parse.urlencode({'email': email}).encode()
    with urllib.request.urlopen(url, data=data) as res:
        print(res.read().decode())
