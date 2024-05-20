#!/usr/bin/python3
"""
rectangle inherits from basegeometry
"""


class BaseGeometry:
    """
    public instances method and exception
    """
    def area(self):
        """
        In this code, raise Exception("area() is not implemented")
        raises an Exception with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    rectangle de inherit BG
    """
    def __init__(self, width, height):
        """
        In this, width and height are initialized integer_validator() makes 
        sure width and height are integers and positive numbers.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
