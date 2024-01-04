#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Class rectangle"""

    def __init__(self, width=0, height=0):
        """Atrributes initializations"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of triangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
