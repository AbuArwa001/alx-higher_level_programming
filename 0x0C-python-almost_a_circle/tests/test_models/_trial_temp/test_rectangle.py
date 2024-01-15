import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        # This method will be called before each test case
        Rectangle._Base__nb_objects = 0

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
