#!/usr/bin/python3
''' module for the `Square Class '''


class Square:
    ''' A Sqaure; a shape whose sides are all of the same length '''
    def __init__(self, size=0):
        '''  Square constructor '''
        self.size = size

    def area(self):
        ''' calculates the area of the square '''
        return self.__size ** 2

    @property
    def size(self):
        ''' gets the length of a side of a square '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' sets the length of the sides of a square '''
        if type(value) not in [int, float]:
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, v):
        ''' compares the are of this square with another; using == '''
        return self.area() == (v.area() if type(v) == Square else v)

    def __ne__(self, v):
        ''' compares the are of this square with another; using != '''
        return self.area() != (v.area() if type(v) == Square else v)

    def __gt__(self, v):
        ''' compares the are of this square with another; using > '''
        return self.area() > (v.area() if type(v) == Square else v)

    def __ge__(self, v):
        ''' compares the are of this square with another; using >= '''
        return self.area() >= (v.area() if type(v) == Square else v)

    def __lt__(self, v):
        ''' compares the are of this square with another; using < '''
        return self.area() < (v.area() if type(v) == Square else v)

    def __le__(self, v):
        ''' compares the are of this square with another; using <= '''
        return self.area() <= (v.area() if type(v) == Square else v)
