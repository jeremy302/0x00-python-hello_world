#!/usr/bin/python3
''' module for the `Square Class '''


class Square:
    ''' A Sqaure; a shape whose sides are all of the same length '''
    def __init__(self, size=0):
        '''  Square constructor '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ''' calculates the area of the square '''
        return self.__size ** 2
