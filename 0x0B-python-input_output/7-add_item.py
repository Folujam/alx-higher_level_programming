#!/usr/bin/python3
"""
load, add, save
"""
import json
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if os.path.exists('add_item.json'):
    load_from_json_file('add_item.json')
else:
    mlist = []
for i in range(1, len(sys.argv)):
    mlist.append(sys.argv[i])
save_to_json_file(mlist, 'add_item.json')
