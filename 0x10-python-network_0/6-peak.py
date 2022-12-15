#!/usr/bin/python3
''' contains find_peak function '''


def find_peak(ls):
    ''' finds a peak in the list '''
    if ls:
        ls.sort()[len(ls) - 1]
        return ls[0]
    return None
