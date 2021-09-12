#!/usr/bin/python3
def max_integer(my_list=[]):
    res = None
    for v in my_list:
        if res is None or v > res:
            res = v
    return res
