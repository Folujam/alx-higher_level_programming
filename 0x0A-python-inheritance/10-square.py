#!/usr/bin/python3
"""
a square module that inherites basegeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this class(sqr) inherites from rectangle and uses the area
    and integer_validator method"""

    def __init__(self, size):
        """inits positive size && uses int_vali to ensure its int"""
        self.__size = abs(size)
        super().integer_validator('size', size)

    def area(self):
        """Calculate the area of a Square"""
        return self.__size ** 2
