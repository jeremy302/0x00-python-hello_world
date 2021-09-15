#!/usr/bin/python3
def weight_average(my_list=[]):
    s = 0
    t = 0
    for v in my_list:
        s += v[0] * v[1]
        t += v[1]
    return s/t if t else s
