#!usr/bin/python3
"""
rectangle inherits from basegeometry
"""


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
