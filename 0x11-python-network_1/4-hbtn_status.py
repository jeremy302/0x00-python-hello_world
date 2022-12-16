#!/usr/bin/python3
''' performs GET request '''
import requests

if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    content = res.text
    print('Body response:')
    print('\t- type:', type(content))
    print('\t- content:', content)
