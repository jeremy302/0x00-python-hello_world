#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) not in [int, float]:
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, v):
        return self.area() == (v.area() if type(v) == Square else v)

    def __ne__(self, v):
        return self.area() != (v.area() if type(v) == Square else v)

    def __gt__(self, v):
        return self.area() > (v.area() if type(v) == Square else v)

    def __ge__(self, v):
        return self.area() >= (v.area() if type(v) == Square else v)

    def __lt__(self, v):
        return self.area() < (v.area() if type(v) == Square else v)

    def __le__(self, v):
        return self.area() <= (v.area() if type(v) == Square else v)
