#!/usr/bin/python3
''' a module for the MyInt class '''


class MyInt(int):
    ''' an int class with inverse equality tests '''
    def __eq__(self, obj):
        ''' inverts == '''
        return super().__ne__(obj)

    def __ne__(self, obj):
        ''' inverts != '''
        return super().__eq__(obj)
