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
        super().__init__(width=size, height=size, x=0, y=0, id=id)
        self.x = x
        self.y = y
        self.size = size

    @property
    def size(self):
        """Get the size of the Square.

        Returns:
            int: The size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square.

        Args:
            value (int): The new size for the Square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is not greater than 0.

        Notes:
            This setter method updates both width and height to maintain
            the Square's dimensions.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        # Update width, height, and size
        self.update(width=value, height=value)
        self.__size = value
        # self.__width = value
        # self.__height = value

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
        super().update(*args, **kwargs)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing the attributes of the instance.
        """
        return super().to_dictionary()
