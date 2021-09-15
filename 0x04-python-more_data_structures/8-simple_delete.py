#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    res = a_dictionary  # .copy()
    if key in res:
        del res[key]
    return res
