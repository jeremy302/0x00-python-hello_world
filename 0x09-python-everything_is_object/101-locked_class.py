#!/usr/bin/python3
''' module for a locked class'''


class LockedClass:
    ''' A class that allows certain attributes to be set '''
    def __setattr__(self, name, value):
        ''' controls which attributes can be set '''
        if name != 'first_name':
            raise AttributeError("object has no attribute '{:s}'".format(name))
        super().__setattr__(name, value)
