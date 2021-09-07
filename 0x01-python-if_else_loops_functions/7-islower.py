#!/usr/bin/python3
def islower(c):
    return bool(type(c) == str and any(_c >= 'a' and _c <= 'z' for _c in c))
