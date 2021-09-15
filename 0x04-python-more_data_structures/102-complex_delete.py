#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    r = {k: v for k, v in a_dictionary.items() if v != value}
    if list(r.keys()) == list(a_dictionary.keys()):
        return a_dictionary
    for k in list(a_dictionary.keys()):
        if k not in r:
            del a_dictionary[k]
    return r
