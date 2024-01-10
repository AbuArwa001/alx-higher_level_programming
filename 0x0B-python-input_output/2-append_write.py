#!/usr/bin/python3
"""
Module containing append_write function to append
text in files
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of the file creates a file if it doesnt exist
    Args:
        filename:
        text:

    Returns:

    """
    written = 0
    with open(filename, 'a', encoding='utf-8') as file:
        written = file.write(text)
    return written
