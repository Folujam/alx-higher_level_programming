#!/usr/bin/python3
"""
student to disk and reload
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

    def reload_from_json(self, json):
        """
        In this code, setattr(self, key, value) sets the attribute key
        of the object self to value. The for loop goes through each key-value
        pair in the json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
