#!/usr/bin/python3
''' a module for the classes: BaseGeometry, Rectangle, and Square'''


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


class Rectangle(BaseGeometry):
    ''' a rectangle class '''
    def __init__(self, width, height):
        ''' constructs a rectangle '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' calculates the area '''
        return self.__width * self.__height

    def __str__(self):
        ''' returns the string representation '''
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)


class Square(Rectangle):
    ''' a square class '''
    def __init__(self, size):
        ''' constructs a square class '''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        ''' returns the string representation '''
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
