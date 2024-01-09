#!/usr/bin/python3
"""
to JSON string
"""
import json


def from_json_string(my_str):
    """
    returns the JSON representation of an object
    """
    re = json.loads(my_str)
    return re
