#!/usr/bin/python3
def islower(c):
    return bool(c in [' '] or any(_c >= 'a' and _c <= 'z' for _c in c))
