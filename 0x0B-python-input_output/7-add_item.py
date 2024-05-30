#!/usr/bin/python3
"""
load, add, save
"""
import sys
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

filen = "add_item.json"
try:
    mlist = load_from_json_file(filen)
except FileNotFoundError:
    mlist = []
for i in range(1, len(sys.argv)):
    mlist.append(sys.argv[i])
save_to_json_file(mlist, filen)
