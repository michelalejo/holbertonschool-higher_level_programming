#!/usr/bin/python3
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

import json
from sys import argv

try:
    my_list = load("add_item.json")
except FileNotFoundError:
    my_list = list()
for i in argv[1:]:
    my_list.append(i)

save(my_list, "add_item.json")
