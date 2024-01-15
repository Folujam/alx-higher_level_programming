#!/usr/bin/python3
"""
base class
"""


class Base:
    """
    in this code, a base is created for whatever number of obj
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        if id is not assigned, it would be increamented by 1
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
