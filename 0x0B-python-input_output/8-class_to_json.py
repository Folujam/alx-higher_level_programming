#!/usr/bin/python3
"""
class to json
"""


def class_to_json(obj):
    """
    function to convert an object's attributes into a dictionary
    """
    return vars(obj)
