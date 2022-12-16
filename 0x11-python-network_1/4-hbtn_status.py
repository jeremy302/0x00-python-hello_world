#!/usr/bin/python3
''' performs GET request '''
import requests

if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    content = res.text
    print('Body response:')
    print('    - type:', type(content))
    print('    - content:', content)
