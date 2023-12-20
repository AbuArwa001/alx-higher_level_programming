#!/usr/bin/python3
#!/usr/bin/python3
"""Squre module and calculates square area"""


class Square:
    """Square of an Area"""
    def __init__(self, size=0):
        """Init the square classs
        Args:
        param1: size is the type int attribute to make it private
        """
        self.__size = size

    @property
    def size(self):
        """Returns Size of the side of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square
        """
        return self.__size * self.__size
