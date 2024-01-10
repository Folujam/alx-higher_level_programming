#!usr/bin/python3
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

    def integer_validation(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
