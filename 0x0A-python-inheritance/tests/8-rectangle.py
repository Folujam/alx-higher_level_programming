#!usr/bin/python3
"""
rectangle inherits from basegeometry
"""


class Rectangle(BaseGeometry):
    """
    rectangle de inherit BG
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
