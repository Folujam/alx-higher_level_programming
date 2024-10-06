#!/usr/bin/python3
"""
base class
"""
import json


class Base:
    """
    in this code, a base is created for whatever number of obj
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        if id is not assigned, it would be increamented by 1
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method returns the JSON string rep of arg"""
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return "[]"
