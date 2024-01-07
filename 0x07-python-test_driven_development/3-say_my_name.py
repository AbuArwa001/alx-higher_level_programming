#!/usr/bin/python3
"""
    Module: 2-say_my_name
    This module provides a function say_my_name(first_name, last_name)
    prints info.

"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
