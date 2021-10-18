#!/usr/bin/python3
''' module for the class: Rectangle '''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle class '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' initializes a rectangle '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, val):
        ''' width setter '''
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, val):
        ''' height setter '''
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def x(self, val):
        ''' x setter '''
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @y.setter
    def y(self, val):
        ''' y setter '''
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        ''' calculates the area '''
        return self.height * self.width

    def display(self):
        ''' prints the rectangle '''
        print(self.y * '\n' + ((self.x * ' ' + '#' * self.width +
                                bool(self.width) * '\n') * self.height)[0:-1])

    def __str__(self):
        ''' returns a string visualization of the rectangle '''
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        ''' updates the rectangle '''
        sz = len(args)
        if sz:
            if sz:
                self.id = args[0]
            if sz > 1:
                self.width = args[1]
            if sz > 2:
                self.height = args[2]
            if sz > 3:
                self.x = args[3]
            if sz > 4:
                self.y = args[4]
        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        ''' converts the rectangle to a string '''
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
