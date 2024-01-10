#!/usr/bin/python3
"""
only sub class of
"""


def inherits_from(obj, a_class):
    """
    In this code, isinstance(obj, a_class) checks if obj is an
    instance of a_class or a subclass of a_class, and type(obj)
    is not a_class checks if obj is not an instance of a_class itself
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
