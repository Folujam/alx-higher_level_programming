#!/usr/bin/python3
"""
my list and test
"""


class MyList(list):
    """
    class of list
    """
    def print_sorted(self):
        """
        In this code, sorted(self) returns a new list
        that contains all items from self (the MyList instance)
        in ascending order. The print() function is used to print
        this sorted list.
        """
        print(sorted(self))
