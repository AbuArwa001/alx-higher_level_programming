#!/usr/bin/python3
"""
module that uses class MyLits
"""


class MyList(list):
    """
        class that inherits class List
    """
    def __init__(self):
        """
            init that initializes with parent class method
        """
        super().__init__()

    def print_sorted(self):
        """
        method that prints list
        Returns:
            None

        """
        if all(isinstance(element, int) for element in self):
            sorted_list = sorted(self)
            print(sorted_list)
        else:
            print("Unable to sort the list: "
                  "All elements must be integers or floats.")
