#!/usr/bin/python3
"""
save object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file
    """
    with open(filename, "w", encoding="utf-8") as afile:
        json.dump(my_obj, afile)
