#!/usr/bin/python3
''' module for the `Square Class '''


class Square:
    ''' A Sqaure; a shape whose sides are all of the same length '''
    def __init__(self, size=0, position=(0, 0)):
        '''  Square constructor '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        ''' prints a square '''
        if self.size == 0:
            print()
        else:
            print("{:s}".format(self.__position[1] * '\n' +
                                (self.__position[0] * ' ' +
                                 '#' * self.__size + '\n') * self.__size)[:-1])

    @property
    def position(self):
        ''' gets the position of the square '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' sets the position of the square '''
        if (type(value) != tuple or len(value) != 2 or type(value[0]) != int or
            type(value[1]) != int or (value[0] < 0 or
                                      value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
