#!/usr/bin/python3
"""
module add attr to class if possible
"""


def add_attribute(obj, key, value):
    """
    function trys to add a new attribute
    to a class, throws Exception on failure
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, key, value)
