#!/usr/bin/python3
"""
exact same object
"""


def is_same_class(obj, a_class):
    """
    In this code, type(obj) returns the class
    of the object obj, and is a_class checks if this
    is the same as a_class.
    """
    return type(obj) is a_class
