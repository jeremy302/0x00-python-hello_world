#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0
    roman_string = roman_string.lower()
    tbl = {'': 0, 'i': 1, 'v': 5, 'x': 10,
           'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    i = 0
    num = 0
    l = len(roman_string)
    while i < l:
        c0 = roman_string[i]
        c1 = roman_string[i + 1] if l - 1 > i else ''
        v0 = tbl[c0]
        v1 = tbl[c1]
        if v1 > v0:
            num += v1 - v0
            i += 1
        else:
            num += v0
        i += 1
    return num
