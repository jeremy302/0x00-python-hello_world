#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        print("{:s}".format(self.__position[1] * '\n' +
                            (self.__position[0] * ' ' +
                             '#' * self.__size + '\n') * self.__size)[:-1])

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        return "{:s}".format(self.__position[1] * '\n' +
                             (self.__position[0] * ' ' +
                             '#' * self.__size + '\n') * self.__size)[:-1]
