#!/usr/bin/python3
''' module for the class: Square '''
from .rectangle import Rectangle


class Square(Rectangle):
    ''' a Square class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' initializes a square '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' gets the string drawing of the square '''
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.height)

    @property
    def size(self):
        ''' size getter '''
        return self.width

    @size.setter
    def size(self, val):
        ''' size setter '''
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        ''' updates the square '''
        sz = len(args)
        if sz:
            if sz:
                self.id = args[0]
            if sz > 1:
                self.size = args[1]
            if sz > 2:
                self.x = args[2]
            if sz > 3:
                self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        ''' gets a dictionary representation of the square '''
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
