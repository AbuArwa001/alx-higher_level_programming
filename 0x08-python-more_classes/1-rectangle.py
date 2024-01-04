#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Class rectangle"""

    def __init__(self, width=0, height=0):
        """Atrributes initializations"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get the width of triangle"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Gets the height"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
