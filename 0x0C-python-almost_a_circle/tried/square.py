#!/usr/bin/python3
"""Module containing class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square contains
    Methods:
        __init__: initializes width
                              height:
                              x, y, and id
        size: size of the square
    Attributes:
        __size-> size
        __x -> x
        __y -> y
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a subclass of Rectangle
        Args:
            x: x-coordinate of the square
            y: y-coordinate of the square
            id: id of the rectangle
        """
        super().__init__(width=size, height=size, x=0, y=0, id=None)
        self.x = x
        self.y = y
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Set the width and height of the rectangle."""
        if isinstance(value, int) and value > 0:
            self.update(height=value, width=value)
            self.__size = value
        else:
            raise TypeError("width must be an integer and > 0")

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance
                        based on the provided arguments.

        Args:
            *args: Variable number of positional arguments
                    representing the values for the attributes.
            **kwargs: Variable number of keyword arguments where:
                            the keys correspond to the attribute names.

        Example:
            sq = Square(1, 2, 3, 4)
                where :*args is the list of arguments - no-keyworded arguments
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            sq.update(10, size=30, x=4, y=5)

        The method allows updating attributes either through \
            positional arguments or keyword arguments.
        For positional arguments, the order should \
            match the attributes: id, width, height, x, y.
        For keyword arguments, the keys should be the attribute \
            names prefixed with '_Rectangle__'. except for size
            which is the Attribute for square class
        Note: If a non-existing attribute is provided in **kwargs, \
            it will be ignored.

        Returns:
            None
        """
        attribute_names = ['id', '_Rectangle__width', '_Rectangle__height', '_Rectangle__x', '_Rectangle__y']
        super().update(*args, **kwargs)
        if 'size' in kwargs:
            print("TRY")
            re_dict = self.__dict__
            size_value = kwargs['size']
            re_dict.update({'_Rectangle__width': size_value, '_Rectangle__height': size_value, })
            self.__size = size_value
            # self.__width = size_value  # Assuming size corresponds to width and height in the Square class
            # self.__height = size_value
            # print(self.__height)
