#!/usr/bin/python3
"""
Module containing to_json_string function to convert
dictionaries too json object
"""
import json


def to_json_string(my_obj):
    """
    function computes JSON representation
    Args:
        my_obj:

    Returns:
        JSON representation

    """
    return json.dumps(my_obj)
