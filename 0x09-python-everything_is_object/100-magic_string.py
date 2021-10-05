#!/usr/bin/python3
def magic_string():
    globals().update({'mag_i': globals().get('mag_i', 0) + 1})
    return ("Holberton, " * (globals().get('mag_i')))[:-2]
