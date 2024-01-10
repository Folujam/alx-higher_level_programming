#!/usr/bin/python3
"""
student to json
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        define your Student class and initialize your
        instance attributes in the __init__ method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        define a to_json method that returns a dictionary
        representation of the Student instance
        """
        return vars(self)
