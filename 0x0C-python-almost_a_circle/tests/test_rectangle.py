#!/usr/bin/python3
"""Unit tests for the Module for the Rectangle class in the shapes module.
This module includes test cases for the Rectangle class,
which is a foundational class for other shapes like Rectangle and Square.
"""

import io
import unittest
from io import StringIO
from unittest.mock import patch
import sys


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Sets up the class for each test"""
        from models.rectangle import Rectangle
        # This method will be called before each test case
        Rectangle._Base__nb_objects = 0
        self.rectz = Rectangle(1, 2, 3, 4, 5)
        sys.stdout.flush()

    def test_input_not_int(self):
        """Test class inputs for rectangle"""
        from models.rectangle import Rectangle
        attributes_to_test = ['height', 'width', 'x', 'y']

        for attribute in attributes_to_test:
            with self.subTest(attribute=attribute):
                with self.assertRaises(TypeError, msg=f"{attribute} "
                                                      f"must be an integer"):
                    # Create a Rectangle object with a non-integer
                    # value for the specified attribute
                    rectangle1 = Rectangle("5", 2, 0, 0, 12)

    def test_value_error(self):
        """Test if ValueError is raised for invalid attribute values"""
        from models.rectangle import Rectangle
        attributes_to_test = ['height', 'width']
        for attribute in attributes_to_test:
            with self.subTest(attribute=attribute):
                with self.assertRaises(ValueError,
                                       msg=f"{attribute} must be > 0"):
                    # Create a Rectangle object with a
                    # non-positive value for the specified attribute
                    rectangle1 = Rectangle(-1, 9)
                    rectangle2 = Rectangle(1, 0)

    def test_negative_x_and_y(self):
        """Test if ValueError is raised for negative x and y values"""
        from models.rectangle import Rectangle
        # Test case with negative values for x and y
        with self.subTest(attribute="x"):
            with self.assertRaises(ValueError, msg="x must be >= 0"):
                Rectangle(5, 10, -2, 3, 7)

        with self.subTest(attribute="y"):
            with self.assertRaises(ValueError, msg="y must be >= 0"):
                Rectangle(5, 10, 2, -3, 7)

    def test_normal_values(self):
        """Test with normal values for height, width, x, and y"""
        from models.rectangle import Rectangle
        rect = Rectangle(5, 10, 2, 3, 7)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 7)

    def test_area_calculation(self):
        """Test the area calculation method"""
        from models.rectangle import Rectangle
        # Case 1: Normal values
        rect1 = Rectangle(5, 10)
        self.assertEqual(rect1.area(), 50)

        # Case 2: Zero width and non-zero height
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect8 = Rectangle(0, 8)
            rect8.area()

        # Case 3: Non-zero width and zero height
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect3 = Rectangle(6, 0)
            rect3.area()

        # Case 4: Zero width and zero height
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect4 = Rectangle(0, 0)
            rect4.area()

        # Case 5: Negative width and non-zero height
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect5 = Rectangle(-3, 12)
            rect5.area()

        # Case 6: Non-zero width and negative height
        with self.assertRaises(ValueError, msg="height must be > 0"):
            rect6 = Rectangle(7, -4)
            rect6.area()

        # Case 7: Negative width and negative height
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect7 = Rectangle(-2, -6)
            rect7.area()

    def test_str_method(self):
        """Test the str method"""
        from models.rectangle import Rectangle
        # Case 1: Normal values
        rect1 = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(rect1), "[Rectangle] (5) 1/2 - 3/4")

        # Case 2: Zero width and non-zero height
        # rect2 = Rectangle(0, 5, 0, 0, 10)
        # self.assertEqual(str(rect2), "[Rectangle] (10) 0/0 - 0/5")

        # Case 3: Non-zero width and zero height
        # rect3 = Rectangle(7, 0, 2, 3, 7)
        # self.assertEqual(str(rect3), "[Rectangle] (7) 2/3 - 7/0")

        # Case 4: Zero width and zero height
        # rect4 = Rectangle(0, 0, 0, 0, 1)
        # self.assertEqual(str(rect4), "[Rectangle] (1) 0/0 - 0/0")

        # Case 5: Negative width and non-zero height
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect5 = Rectangle(-3, 8, 1, 1, 20)
            str(rect5)

        # Case 6: Non-zero width and negative height
        with self.assertRaises(ValueError, msg="height must be > 0"):
            rect6 = Rectangle(4, -5, 2, 2, 15)
            str(rect6)

        # Case 7: Negative width and negative height
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect7 = Rectangle(-2, -6, 3, 4, 8)
            str(rect7)

    def test_display_method(self):
        """Test the display method"""
        from models.rectangle import Rectangle
        # Case 1: Normal values
        rect1 = Rectangle(3, 4, 1, 2, 5)
        expected_output1 = "\n\n ###\n ###\n ###\n ###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output1)

        # Case 2: Non-zero x and y values
        rect2 = Rectangle(4, 3, 2, 1, 7)
        expected_output2 = "\n  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output2)

        # Case 3: Zero x and non-zero y values
        rect3 = Rectangle(2, 2, 0, 3, 9)
        expected_output3 = "\n\n\n##\n##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect3.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output3)

        # Case 4: Non-zero x and zero y values
        rect4 = Rectangle(3, 5, 2, 0, 12)
        expected_output4 = "  ###\n  ###\n  ###\n  ###\n  ###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect4.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output4)

    def test_update_method(self):
        """Test the update method"""
        # Test case to check if the update method correctly
        # updates attributes using positional arguments
        self.rectz.update(10, 20, 30, 4, 5)
        self.assertEqual(str(self.rectz), "[Rectangle] (10) 4/5 - 20/30")

        # Test case to check if the update method
        # correctly updates attributes using keyword arguments
        self.rectz.update(width=40, height=50, x=6, y=7)
        self.assertEqual(str(self.rectz), "[Rectangle] (10) 6/7 - 40/50")

        # Test case to check if the update method
        # correctly handles non-existing attributes in kwargs
        self.rectz.update(width=60, depth=70, x=8, y=9)
        self.assertEqual(str(self.rectz), "[Rectangle] (10) 8/9 - 60/50")

        # Test case to check if the update method
        # correctly handles both positional and keyword arguments
        self.rectz.update(100, width=80, height=90, x=10, y=11)
        self.assertEqual(str(self.rectz), "[Rectangle] (100) 10/11 - 80/90")


if __name__ == '__main__':
    unittest.main()
