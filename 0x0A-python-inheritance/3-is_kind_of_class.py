#!/usr/bin/python3
''' a module for the class: is_kind_of_class '''


def is_kind_of_class(obj, a_class):
    ''' checks if obj's type is the same of an instance of a_class '''
    return issubclass(type(obj), a_class)
