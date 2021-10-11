#!/usr/bin/python3
''' a module for the function: add_attribute '''


def add_attribute(obj, key, val):
    ''' sets an attribute of an object if possible '''
    if getattr(obj, '__dict__', None) is None:
        raise TypeError("can't add new attribute")
    setattr(obj, key, val)
