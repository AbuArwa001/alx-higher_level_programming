#!/usr/bin/python3
"""
Module containing save_to_json_file function to save to json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file
    Args:
        my_obj:
        filename:

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
