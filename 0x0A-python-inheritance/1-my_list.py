#!/usr/bin/python3
"""
my list and test
"""


class MyList(list):
    """
    class of list
    """

    def print_sorted(self):
        """inherited list is from baseclass is sorted"""
        print(sorted(self))
