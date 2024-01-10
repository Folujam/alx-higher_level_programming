#!/usr/bin/python3
"""
student to JSON with filter
"""


def to_json(self, attrs=None):
    """
    In this code, isinstance(attrs, list) checks if attrs is a list,
    and all(isinstance(i, str) for i in attrs) checks if all elements
    in attrs are strings. If both conditions are true, it returns a
    dictionary with only those attributes. The hasattr(self, i) function
    checks if the attribute exists in the object. If attrs is not
    a list of strings, it returns a dictionary with all attributes
    using the vars() function.
    """
    if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
        return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
    else:
        return vars(self)
