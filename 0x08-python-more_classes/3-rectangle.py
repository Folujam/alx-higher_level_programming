#!/usr/bin/python3
"""
write a class rectangle
def width, height, return area, return perimeter
"""


class Rectangle:
    """
    a defined class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width is 0 or self.height is 0:
            return 0
        p = self.height + self.width
        return 2 * p

    def __str__(self):
        str_rp = ''
        if self.width is not 0 or self.height is not 0:
            for i, _ in enumerate(range(self.height)):
                str_rp += '#' * self.width
                if i != self.height - 1:
                    str_rp += '\n'
        return str_rp
