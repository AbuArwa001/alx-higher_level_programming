#!/usr/bin/python3
"""Squre module and calculates square area"""


class Square:
    """Square of an Area"""
    def __init__(self, size=0, position=(0, 0)):
        """Init the square class
        Args:
        param1: size is the type int attribute to make it private
        param2: posiition of the iterator
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Returns Size of the side of the square"""
        return self.__size

    @size.setter
    def position(self, value):
        """"set position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with # character in standard output.

        If the size is 0, prints an empty line.
        Otherwise, prints the square with proper indentation and # characters.
        """
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
