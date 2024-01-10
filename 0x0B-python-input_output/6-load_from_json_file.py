#!/usr/bin/python3
"""
Module that contains load_from_json_file to
operate on JSON FILES
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    Args:
        filename: Name of the file

    Returns:
        OBJECT; ie, lists, dictionaries

    """
    oj = ""
    with open(filename, 'r', encoding='utf-8') as f:
        oj = json.loads(f.read())
    return oj
