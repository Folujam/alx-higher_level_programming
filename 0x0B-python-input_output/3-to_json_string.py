#!/usr/bin/python3
import json
"""
to JSON string
"""


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    """
    re = json.dumps(my_obj)
    return re
