#!/usr/bin/python3
"""Module for testing the Rectangle class"""
import unittest
from io import StringIO
import sys
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

    def test_area_calculation(self):
        # Test case to check if the area method correctly calculates the area of a rectangle
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

    def test_display_method(self):
        # Test case to check if the display method correctly prints the rectangle
        # Case 1: Normal values
        rect1 = Rectangle(3, 4)
        captured_output1 = StringIO()
        sys.stdout = captured_output1
        rect1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output1.getvalue(), "###\n###\n###\n###\n")

        # Case 2: Zero width and non-zero height
        # rect2 = Rectangle(0, 5)
        # captured_output2 = StringIO()
        # sys.stdout = captured_output2
        # rect2.display()
        # sys.stdout = sys.__stdout__
        # self.assertEqual(captured_output2.getvalue(), "\n\n\n\n\n")
        #
        # # Case 3: Non-zero width and zero height
        # rect3 = Rectangle(7, 0)
        # captured_output3 = StringIO()
        # sys.stdout = captured_output3
        # rect3.display()
        # sys.stdout = sys.__stdout__
        # self.assertEqual(captured_output3.getvalue(), "\n\n\n\n\n\n\n")
        #
        # # Case 4: Zero width and zero height
        # rect4 = Rectangle(0, 0)
        # captured_output4 = StringIO()
        # sys.stdout = captured_output4
        # rect4.display()
        # sys.stdout = sys.__stdout__
        # self.assertEqual(captured_output4.getvalue(), "")

        # Case 5: Negative width and non-zero height
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect5 = Rectangle(-3, 8)
            rect5.display()

        # Case 6: Non-zero width and negative height
        with self.assertRaises(ValueError, msg="height must be > 0"):
            rect6 = Rectangle(4, -5)
            rect6.display()

        # Case 7: Negative width and negative height
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rect7 = Rectangle(-2, -6)
            rect7.display()


if __name__ == '__main__':
    unittest.main()
