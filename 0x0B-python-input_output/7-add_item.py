#!/usr/bin/python3
"""
load, add, save
"""
import sys
import json


def load_from_json_file(filename):
    """
     creates an Object from a “JSON file”
    """
    with open(filename, "r") as afile:
        return json.load(afile)


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file
    """
    with open(filename, "w", encoding="utf-8") as afile:
        json.dump(my_obj, afile)


try:
    mlist = load_from_json_file('add_item.json')
except FileNotFoundError:
    mlist = []
for i in range(1, len(sys.argv)):
    mlist.append(sys.argv[i])
save_to_json_file(mlist, 'add_item.json')
