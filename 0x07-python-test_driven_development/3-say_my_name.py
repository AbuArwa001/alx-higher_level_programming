#!/usr/bin/python3
"""
    Module: 2-say_my_name
    This module provides a function say_my_name(first_name, last_name)
    prints info.

"""


def say_my_name(first_name, last_name=""):
    """
    Function for introduction.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    introduction = f"My name is {first_name} {last_name}" \
        if first_name else f"My name is {last_name}"
    print(introduction)
