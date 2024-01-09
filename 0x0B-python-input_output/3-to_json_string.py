#!/usr/bin/python3
"""
to JSON string
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    """
    re = json.dumps(my_obj)
    return re
