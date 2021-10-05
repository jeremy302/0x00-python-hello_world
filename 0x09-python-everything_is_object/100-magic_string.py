#!/usr/bin/python3
def magic_string():
    magic_string.__dict__['i'] = magic_string.__dict__.get('i', 0) + 1
    return ("BestSchool, " * magic_string.__dict__['i'])[:-2]
