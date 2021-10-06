#!/usr/bin/python3
'''This modules contains a function to add integers

Example:
add_integer(1, 2) -> 3
'''


def add_integer(a, b=98):
    ''' adds 2 integers: a and b.

    if any of the argument is a float,
    it is first casted to an integer.

    Args:
        a (int): an integer
        b (int): an integer
    '''
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
