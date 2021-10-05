#!/usr/bin/python3
''' module for a locked class'''


class LockedDict(dict):
    ''' A restrictive dict '''
    def __setitem__(self, name, value):
        ''' sets an key-value pair '''
        if name != 'first_name':
            raise AttributeError("object has no attribute {}".format(
                repr(name)))
        super().__setitem__(name, value)


class LockedClass:
    ''' A class that allows certain attributes to be set '''

    def __init__(self):
        ''' class constructor '''
        self.__dict__ = LockedDict(self.__dict__)

    def __setattr__(self, name, value):
        ''' controls which attributes can be set '''
        if type(self.__dict__) == LockedDict and name != 'first_name':
            raise AttributeError("object has no attribute {}".format(
                repr(name)))
        super().__setattr__(name, value)

    def __setitem__(self, name, value):
        ''' controls which attributes can be set with index notation '''
        if type(self.__dict__) == LockedDict and name != 'first_name':
            raise AttributeError("object has no attribute {}".format(
                repr(name)))
        self.first_name = value
