#!/usr/bin/python3
def islower(c):
    if c:
        c = c[0]
    return bool(bool(c) and ord(c) >= ord('a') and ord(c) <= ord('z'))
