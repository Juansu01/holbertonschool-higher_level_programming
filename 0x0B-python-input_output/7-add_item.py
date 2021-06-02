#!/usr/bin/python3
""" This module imports functions from 5-save_to_json_file
and 6-load_from_json_file """
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    new_list = load_from_json_file('add_item.json')
except:
    new_list = []

for arguments in range(1, len(argv)):

    new_list.append(argv[arguments])

save_to_json_file(new_list, 'add_item.json')
