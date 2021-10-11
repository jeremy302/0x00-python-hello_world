#!/usr/bin/python3
''' module for the function: inherits_from '''


def inherits_from(obj, a_class):
    ''' checks if obj's type is a descenedant of a_claass '''
    return type(obj) is not a_class and issubclass(type(obj), a_class)
