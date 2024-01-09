#!/usr/bin/python3
"""
    module for opening and reading files
"""


def read_file(filename=""):
    """Read file from file system"""
    with open(filename, 'r') as f:
        print(f.read())
