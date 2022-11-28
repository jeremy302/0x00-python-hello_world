#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    res = [0, 0]
    for i in range(2):  # for the possible 2 elements
        # add a[0] or a[1] if tuple_a is big enough
        res[i] += tuple_a[i] if len_a > i else 0
        # add tuple_b[0] or tuple_b[1] if tuple_b is big enough
        res[i] += tuple_b[i] if len_b > i else 0
    return tuple(res)
