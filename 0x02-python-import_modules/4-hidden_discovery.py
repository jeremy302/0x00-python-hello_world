#!/usr/bin/python3
import sys
import re
import hidden_4

if __name__ == '__main__':
    with open('hidden_4.pyc', 'rb') as f:
        h = f.read()
        for n in sorted(re.findall(rb'\w{3,}', h)):
            if n not in [b'hidden_4', b'module'] and\
               not n.startswith(b'__'):
                print(n.decode())
