#!/usr/bin/python3
"""
this reads a file
"""


def read_file(filename=""):
    """
    this function opens a file in read mode and prints it
    """
    with open(filename, encoding="utf-8") as afile:
        re = afile.read()
        print(re, end="")
