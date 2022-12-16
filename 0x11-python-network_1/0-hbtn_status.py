#!/usr/bin/python3
# performs GET request
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print('Body response:')
        print('    - type:', type(content))
        print('    - content:', content)
        print('    - utf8 content:', content.decode())
