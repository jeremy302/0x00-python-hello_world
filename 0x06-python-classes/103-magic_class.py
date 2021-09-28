#!/usr/bin/python3
''' module for the `Magic Class '''


import math


class MagicClass:
    ''' A class to calculate the area and circumference of a circle '''
    def __init__(self, radius=0):
        ''' constructs a circle '''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        ''' calculates the area of the circle '''
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        ''' calculates the circumference of the circle '''
        return 2 * math.pi * self.__radius
