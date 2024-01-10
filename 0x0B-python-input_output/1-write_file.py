#!/usr/bin/python3
"""
Module containing a write_file function
"""


def write_file(filename="", text=""):
    """
    writing text to file name overriding previous content
    Args:
        filename: name of the file
        text: text to write

    Returns:
        the number of characters written:

    """
    written = 0
    with open(filename, 'w', encoding='utf-8') as file:
        written = file.write(text)
    return written
