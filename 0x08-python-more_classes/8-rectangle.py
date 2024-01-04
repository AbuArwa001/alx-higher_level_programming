#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Class rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Attributes initializations"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        rows = [str(self.print_symbol) * self.__width
                for _ in range(self.__height)
                ]
        return "\n".join(rows)

    def __repr__(self):
        """Representation string information for a class"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletion of an instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("ect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
