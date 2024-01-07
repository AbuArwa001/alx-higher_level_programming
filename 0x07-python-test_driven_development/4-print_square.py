#!/usr/bin/python3
"""
    Module: print_square
    This module provides a function print_square(size)
    prints a square.
"""


def print_square(size):
    """
    function that prints a square with the character #.
    Args:
        size: length and width of the square

    Returns:
        None
    Raises:
        TypeError: is raised when size is ot integer
                 :  size is a float and is less than 0
        ValueError: if size is less than 0

    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [print("#" * size) for _ in range(size)]
    pass
