#!/usr/bin/python3
''' a module for the classes: BaseGeometry, Rectangle, and Square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' a square class '''
    def __init__(self, size):
        ''' constructs a square class '''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
