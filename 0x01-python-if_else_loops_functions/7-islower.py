#!/usr/bin/python3
def islower(c):
    return bool(any(_c >= 'a' and _c <= 'z' for _c in c))
