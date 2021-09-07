#!/usr/bin/python3
def islower(c):
    return (bool(c) and type(c) == str and len(c) == 1 and
                ord(c) >= ord('a') and ord(c) <= ord('z'))
