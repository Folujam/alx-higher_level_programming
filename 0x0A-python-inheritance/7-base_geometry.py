#!/usr/bin/python3
"""
geometry module
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
