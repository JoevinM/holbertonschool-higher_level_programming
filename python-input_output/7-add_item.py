#!/usr/bin/python3

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    list_to_add = load_from_json_file("add_item.json")
except FileNotFoundError:
    list_to_add = []

for arg in sys.argv[1:]:
    list_to_add.append(arg)

save_to_json_file(list_to_add, "add_item.json")
