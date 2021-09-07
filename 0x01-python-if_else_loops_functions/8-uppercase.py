#!/usr/bin/python3
def uppercase(str):
    print('{:s}'.format(''.join([(c if c < 'a' or c > 'z'
                                  else chr(ord(c) - 32)) for c in str])))
