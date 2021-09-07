#!/usr/bin/python3
def magic_calculation(a=0, b=1, c=2):
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b - c)
# dis.dis(magic_calculation)
