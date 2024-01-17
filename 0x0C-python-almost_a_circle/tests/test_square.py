import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        # This method will be called before each test case
        self.default_square = Square(5, 1, 2, 3)

    def test_size_property(self):
        # Test case to check if the size property works as expected
        self.assertEqual(self.default_square.size, 5)

        self.default_square.size = 8
        self.assertEqual(self.default_square.size, 8)

        with self.assertRaises(TypeError, msg="width must be an integer and > 0"):
            self.default_square.size = -3

    def test_init(self):
        # Test case to check if the __init__ method initializes the Square object correctly
        square = Square(4, 2, 3, 7)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 7)

    def test_size_setter(self):
        # Test case to check if the size setter updates the width and height correctly
        square = Square(6, 1, 2, 8)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

        with self.assertRaises(TypeError, msg="Size must be a positive integer."):
            square.size = -5


if __name__ == '__main__':
    unittest.main()
