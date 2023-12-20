#!/usr/bin/python3
"""Square module and calculates square area"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Init the square class
        Args:
        param1: size is the type int attribute to make it private
        param2: posiition of the iterator
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns Size of the side of the square"""
        return self.__size

    @property
    def position(self):
        """Returns Size of the side of the square"""
        return self.__position

    @size.setter
    def size(self, value):
        """"set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """"set position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Str to get information about the class"""
        if self.__size != 0:
            [print("")for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ""
