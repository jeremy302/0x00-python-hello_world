#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    ls = my_list.copy()
    my_list.clear()
    for i in range(len(ls)):
        if i != idx:
            my_list.append(ls[i])
    return my_list
