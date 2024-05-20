#!/usr/bin/python3
"""
creates a myint inherited from Int and it rebels
"""


class MyInt(int):
    """
    this Class behaves like an int but Rebels
    """

    def __eq__(self, other_num):
        return super().__ne__(other_num)

    def __ne__(self, other_num):
        return super().__eq__(other_num)
