#!/usr/bin/python3
"""
rectangle inherits from basegeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    rectangle de inherit BG
    """
    def __init__(self, width, height):
        """
        In this code, self.integer_validator("width", width)
        and self.integer_validator("height", height) call the
        integer_validator method to validate width and height,
        and self.__width = width and self.__height = height assign
        these values to private instance variables
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This method return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This method return the representation of the Rectangle"""
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)