#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ls = my_list.copy()
    if idx >= 0 and idx < len(ls):
        ls[idx] = element
    return ls
