#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("You can only create 'first_name' attribute")
        self.__dict__[name] = value
