#!/usr/bin/python3


import json
import sys
import os.path
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file


filename = "add_item.json"
my_list = []

if os.path.isfile(filename):
    with open(filename, 'r+') as f:
        result = f.read()
        if result != "":
            my_list = json.loads(result)
with open(filename, 'w') as f:
    for i, arg in enumerate(sys.argv):
        if i > 0:
            my_list.append(arg)
    f.write(json.dumps(my_list))
