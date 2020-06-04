#!/usr/bin/python3
"""
Module to manage file.
"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
filename = "add_item.json"
Args = sys.argv[1:]
try:
    Content = load_from_json_file(filename)
except FileNotFoundError:
    Content = []
Added = Content + Args
save_to_json_file(Added, "add_item.json")
