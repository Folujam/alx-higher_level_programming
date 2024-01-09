#!/usr/bin/python3
"""
load, add, save
"""
import sys
import os

from 6-load_from_json_file import load_from_json_file

from 5-save_to_json_file import save_to_json_file


if os.path.exists('add_item.json'):
    load_from_json_file('add_item.json')
else:
    mlist = []

for i in range(1, len(sys.argv)):
    mlist.append(sys.argv[i])
save_to_json_file(mlist, 'add_item.json')
