#!/usr/bin/python3
"""Square module and calculates square area"""


class Square:
    """Square of an Area"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns Size of the side of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """"set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Other of the square show equal
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Other of the square show equal
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Other of the square show equal
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Other of the square show equal
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Other of the square show equal
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Other of the square show equal
        """
        return self.area() >= other.area()
