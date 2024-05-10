#!/usr/bin/python3

"""
this is to add two integers and nothing else
"""


def add_integer(a, b=98):
    """ this function checks & ensures a&b are integers,
    if they are floats - converts them to int by rounding them down.
    returns the sum.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
