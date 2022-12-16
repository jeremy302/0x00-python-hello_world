#!/usr/bin/python3
''' githup user api '''
import sys
import requests

if __name__ == '__main__':
    user, passwd = sys.argv[1:3]
    res = requests.get('https://api.github.com/user', auth=(user, passwd))
    if res.ok:
        print(res.json()['id'])
    else:
        print('None')
