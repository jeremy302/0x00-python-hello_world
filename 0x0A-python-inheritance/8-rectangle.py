#!/usr/bin/python3
''' a module for the classes: BaseGeometry and Rectangle'''


class BaseGeometry:
    ''' a geometry class '''

    def area(self):
        ''' calculates the area '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' validates an integer '''
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    ''' a rectangle class '''
    def __init__(self, width, height):
        ''' constructs a rectangle '''
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if width <= 0:
            raise ValueError('width must be greater than 0')
        if height <= 0:
            raise ValueError('height must be greater than 0')
        self.__width = width
        self.__height = height
