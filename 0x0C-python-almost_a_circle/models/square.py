#!/usr/bin/python3
"""
this is Square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this is the definition of Sqaure which inherits from 
    Rectangle(Base)
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width=size, height=size)
