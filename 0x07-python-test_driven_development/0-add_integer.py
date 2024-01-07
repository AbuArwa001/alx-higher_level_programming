#!/usr/bin/python3
"""
    Module for carrying out mathematics calculations
    This module provides a function add_integer(a, b=98):
    Returns: the sum of two numbers.
    """


def add_integer(a, b=98):
    """
    Adds two integers. and Returns: int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
