#!/usr/bin/python3
'''This modules contains a function to get the max integer in a list

Example:
max_integer([1, 2, 3]) -> 3
'''


def max_integer(list=[]):
    ''' gets the max integer in a list

    The biggest integer in the list is returned.
    None is returned if the list is empty

    Args:
        list (list): list to look through
    '''
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
