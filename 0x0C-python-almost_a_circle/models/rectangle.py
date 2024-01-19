#!/usr/bin/python3
"""Module containing class Rectangle"""
import sys

# sys.path.append("/models/")
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle contains
    Methods:
        __init__: initializes width
                              height:
                              x, y, and id
    Attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a subclass of base
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x-coordinate of the rectangle
            y: y-coordinate of the rectangle
            id: id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates area of a rectangle
        Returns:
            Area of a rectangle

        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        Returns:
            None

        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x, end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Creates a string info.

        Returns:
            Class info string.
        """
        # from .rectangle import Rectangle

        # if isinstance(self, Square) or size_in_args:
        from .square import Square
        shape_type = 'Square' if (type(self) is Square
                                  or (type(self) is self.__class__ and
                                      self.width == self.height)) \
            else 'Rectangle'

        dimensions = f"{self.width}" if shape_type == 'Square' \
            else f"{self.width}/{self.height}"

        return f"[{shape_type}] ({self.id}) {self.x}/{self.y} - {dimensions}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance
                    based on the provided arguments.

        Args:
            *args: Variable number of positional arguments
                representing the values for the attributes.
            **kwargs: Variable number of keyword arguments
                where the keys correspond to the attribute names.

        Example:
            rect = Rectangle(1, 2, 3, 4, 5)
            rect.update(10, width=20, height=30, x=4, y=5)

        The method allows updating attributes either
                through positional arguments or keyword arguments.
        For positional arguments, the order should
            match the attributes: id, width, height, x, y.
        For keyword arguments, the keys should be the
            attribute names prefixed with '_Rectangle__'.
        Note: If a non-existing attribute is provided
            in **kwargs, it will be ignored.

        Returns:
            None
        """
        from .square import Square
        size_in_args = 'size' in kwargs

        if not args and not kwargs:
            return  # No arguments provided, nothing to update
        # print(size_in_args)
        if type(self) is Square or size_in_args:
            self.__class__ = Square
            attribute_names = ['id', '_Square__size',
                               '_Rectangle__x', '_Rectangle__y']
        else:
            attribute_names = ['id', '_Rectangle__width', '_Rectangle__height',
                               '_Rectangle__x', '_Rectangle__y']

        for index, item in enumerate(args):
            setattr(self, attribute_names[index], item)

        for key, value in kwargs.items():
            if key in dir(self):
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Returns a dictionary representation of the instance.

            Returns:
                dict: A dictionary containing the attributes of the instance.

            This method creates a dictionary representation of the instance,
            including the common attributes 'id', 'x', and 'y'. Depending on
            the instance type (either a Rectangle or a Square), additional
            attributes such as 'width' and 'height' or 'size' are included in
            the dictionary.

            Example:
                For a Rectangle instance:
                >>> rect = Rectangle(id=1, x=2, y=3, width=4, height=5)
                >>> rect.to_dictionary()
                {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}

                For a Square instance:
                >>> square = Square(id=1, x=2, y=3, size=4)
                >>> square.to_dictionary()
                {'id': 1, 'x': 2, 'y': 3, 'size': 4, 'width': 4, 'height': 4}
            """
        from .square import Square
        dic = {
            'id': self.id,
            'x': self.x,
            'y': self.y,
        }

        if isinstance(self, Square):
            dic['size'] = self.size
            dic['width'] = self.size
            dic['height'] = self.size
        else:
            dic['width'] = self.width
            dic['height'] = self.height

        return dic
