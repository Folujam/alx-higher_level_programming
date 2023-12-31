#!/usr/bin/python3
"""
 a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception
if size is less than 0, raise a ValueError exception
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self):returns the current square area
Public instance method: def my_print(self):
prints in stdout the square with the character #:
if size is equal to 0, print an empty line
"""


class Square:
    """
    private instance attribute: size
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size > 0:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
