#!/usr/bin/python3
def islower(c):
    return bool(type(c) == str and len(c) == 1 and c >= 'a' and c <= 'z')
