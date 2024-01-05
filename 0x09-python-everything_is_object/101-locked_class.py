#!/usr/bin/python3
"""
docu goes here
"""
class LockedClass:
    """
    docu
    """
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        self.__dict__[name] = value
