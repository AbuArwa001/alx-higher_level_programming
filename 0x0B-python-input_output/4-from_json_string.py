#!/usr/bin/python3
"""
Module containing from_json_string function
to convert from json string
"""
import json


def from_json_string(my_str):
    """
    Converts string from json to normal string
    Args:
        my_str:

    Returns:
        string

    """
    return json.loads(my_str)
