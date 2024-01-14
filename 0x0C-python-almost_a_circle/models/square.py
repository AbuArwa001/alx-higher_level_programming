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
        Updates the attributes of the Rectangle instance
                        based on the provided arguments.

        Args:
            *args: Variable number of positional arguments
                    representing the values for the attributes.
            **kwargs: Variable number of keyword arguments where:
                            the keys correspond to the attribute names.

        Example:
            rect = Rectangle(1, 2, 3, 4, 5)
            rect.update(10, width=20, height=30, x=4, y=5)

        The method allows updating attributes either through \
            positional arguments or keyword arguments.
        For positional arguments, the order should \
            match the attributes: id, width, height, x, y.
        For keyword arguments, the keys should be the attribute \
            names prefixed with '_Rectangle__'.
        Note: If a non-existing attribute is provided in **kwargs, \
            it will be ignored.

        Returns:
            None
        """
        width = '_Rectangle__width'
        height = '_Rectangle__height'
        size = '_Square__size'
        x = '_Rectangle__x'
        y = '_Rectangle__y'
        ls = ['id', width, height, x, y]
        re_dict = self.__dict__
        key = ""
        if not args:
            for item in kwargs:
                key = "_Rectangle__" + item if item != 'size' else "_Square__" + item
                if key in re_dict:
                    if key == '_Square__size':
                        # print(item)
                        re_dict.update({width: kwargs.get(item)})
                        re_dict.update({height: kwargs.get(item)})
                    re_dict.update({key: kwargs.get(item)})
                key = ""
                # re_dict[ls[index]] = item
        else:
            ls1 = ['id', size, x, y]
            for index, item in enumerate(args):
                if ls1[index] == size:
                    re_dict[ls1[index]] = item
                    re_dict[ls[index]] = item
                    re_dict[ls[index + 1]] = item
                    continue
                re_dict[ls1[index]] = item
