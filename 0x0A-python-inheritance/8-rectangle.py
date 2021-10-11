#!/usr/bin/python3
''' a module for the classes: BaseGeometry and Rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' a rectangle class '''
    def __init__(self, width, height):
        ''' constructs a rectangle '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
