#!/usr/bin/python3
''' contains find_peak function '''


def find_peak(list_of_integers):
    ''' finds a peak in the list '''
    return sorted(list_of_integers or [None])[len(list_of_integers) - 1]
