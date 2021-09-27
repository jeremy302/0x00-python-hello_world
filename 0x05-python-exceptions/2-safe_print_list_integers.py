#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        v = my_list[i]
        try:
            print('{:d}'.format(v), end='')
            c += 1
        except:
            pass
    print()
    return c
