#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = a_dictionary.copy()
    for k in res:
        res[k] *= 2
