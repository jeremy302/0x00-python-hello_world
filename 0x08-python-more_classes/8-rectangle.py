#!/usr/bin/python3
''' module for a rectangle class '''


class Rectangle:
    ''' a rectangle class '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' instantiates a rectangle '''
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        ''' gets the width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' sets the width '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' gets the height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' sets the height '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' calculates the rectangle's area '''
        return self.height * self.width

    def perimeter(self):
        ''' calculates the reactangle's perimeter '''
        return 0 if not self.height or not self.width else \
            self.height * 2 + self.width * 2

    def __str__(self):
        ''' returns a string form of the rectangle '''
        return (('#' * self.width +
                 bool(self.width) * '\n') * self.height)[0:-1]

    def __repr__(self):
        ''' returns the string representation of the rectangle '''
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        ''' destructor for the rectangle '''
        print('Bye rectangle...')
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' compares the area of 2 rectangles '''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
