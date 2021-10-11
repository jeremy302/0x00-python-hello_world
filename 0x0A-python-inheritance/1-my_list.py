#!/usr/bin/python3
''' a module for the function: print_sorted() '''


class MyList(list):
    ''' a list subclass '''
    def print_sorted(self):
        ''' prints the list in ascending order '''
        print(sorted(self))
