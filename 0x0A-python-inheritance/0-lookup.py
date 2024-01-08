#!/usr/bin/python3
"""
    Modules  that contains lookup function
"""


def lookup(obj):
    """
    function that returns the list of available attributes and methods of an object:
    Args:
        obj:

    Returns:
        returns the list of available attributes

    """
    return dir(obj)
