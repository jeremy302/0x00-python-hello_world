#!/usr/bin/python3
'''This modules contains a function to print a name

Example:
say_my_name('john', 'smith') -> "My name is john smith"
'''


def say_my_name(first_name, last_name=""):
    ''' prints a name

    The names must be strings, otherwise an exception is raised.
    names can be empty

    Args:
        first_name (str): first name
        last_name (str): last name
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
