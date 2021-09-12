#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l = max(len(tuple_a), len(tuple_b))
    res = [0, 0]
    for i in range(2):
        res[i] += (tuple_a[i] if len(tuple_a) > i else 0) +\
            (tuple_b[i] if len(tuple_b) > i else 0)
    return tuple(res)
