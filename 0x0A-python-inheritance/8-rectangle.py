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
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = int(width)
        self.__height = int(height)
