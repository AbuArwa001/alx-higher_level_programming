#!/usr/bin/python3
"""Module for testing the Rectangle class"""
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        # This method will be called before each test case
        Rectangle._Base__nb_objects = 0

    def test_input_not_int(self):
        attributes_to_test = ['height', 'width', 'x', 'y']

        for attribute in attributes_to_test:
            with self.subTest(attribute=attribute):
                with self.assertRaises(TypeError, msg=f"{attribute} must be an integer"):
                    # Create a Rectangle object with a non-integer value for the specified attribute
                    rectangle1 = Rectangle("5", 2, 0, 0, 12)

    def test_value_error(self):
        attributes_to_test = ['height', 'width']
        for attribute in attributes_to_test:
            with self.subTest(attribute=attribute):
                with self.assertRaises(ValueError, msg=f"{attribute} must be > 0"):
                    # Create a Rectangle object with a non-positive value for the specified attribute
                    rectangle1 = Rectangle(-1, 9)
                    rectangle2 = Rectangle(1, 0)

    def test_negative_x_and_y(self):
        # Test case with negative values for x and y
        with self.subTest(attribute="x"):
            with self.assertRaises(ValueError, msg="x must be >= 0"):
                Rectangle(5, 10, -2, 3, 7)

        with self.subTest(attribute="y"):
            with self.assertRaises(ValueError, msg="y must be >= 0"):
                Rectangle(5, 10, 2, -3, 7)

    def test_normal_values(self):
        # Test case with normal values for height, width, x, and y
        rect = Rectangle(5, 10, 2, 3, 7)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 7)


if __name__ == '__main__':
    unittest.main()
