#!/usr/bin/python3
"""
write to a file
"""


def write_file(filename="", text=""):
    """
    function writes a string to a txtfile and returns num of chars
    """
    with open(filename, mode="w", encoding="utf-8") as afile:
        return afile.write(text)
