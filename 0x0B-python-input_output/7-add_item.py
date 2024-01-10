#!/usr/bin/python3
"""
Module containing add_to_list function
                    and imports to manipulate JSON FILES
"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == '__main__':
    import sys
    import os

    my_list = []
    for i, arg in enumerate(sys.argv):
        if i != 0:
            my_list.append(arg)
    filename = "add_item.json"
    my_list1 = []
    if os.path.getsize(filename) > 0:
        my_list1 = load_from_json_file(filename)
    my_list1 += my_list
    save_to_json_file(my_list1, filename)
