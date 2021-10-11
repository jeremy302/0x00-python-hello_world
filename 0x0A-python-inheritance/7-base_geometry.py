#!/usr/bin/python3
''' a module for the class BaseGeometry '''


class BaseGeometry:
    ''' a geometry class '''
    def area(self):
        ''' calculates the area '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' validates an integer '''
        if not issubclass(type(value), int):
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
