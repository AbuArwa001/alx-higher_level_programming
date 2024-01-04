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

    def area(self):
        """Calculates Area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
    # def __str__(self):
    #     strn = ""
    #     for i in range(self.__height):
    #         for j in range(self.__width):
    #             strn += "#"
    #         if i + 1 != self.__height:
    #             strn += "\n"
    #     rows = ["#" * self.__width for _ in range(self.__height)]
    #     return f"{rows}"

    def __str__(self):
        """Str string information for a class"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        """Representation string information for a class"""
        return f"Rectangle({self.__width}, {self.__height})"
