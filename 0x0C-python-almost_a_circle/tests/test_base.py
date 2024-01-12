#!/usr/bin/python3
"""Module for testing the Base class"""

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""
    def setUp(self):
        # This method will be called before each test case
        Base._Base__nb_objects = 0

    def test_instance_creation_with_id(self):
        """Test instance creation with a specified id"""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_instance_creation_without_id(self):
        """Test instance creation without a specified id"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_unique_ids(self):
        """Test if unique ids are assigned to instances"""
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_nb_objects_private_attribute(self):
        """Test if __nb_objects is a private attribute"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_nb_objects_initial_value(self):
        """Test if __nb_objects is initially 0 if id not null"""
        b = Base(2)
        self.assertEqual(type(b)._Base__nb_objects, 0)

    def test_nb_objects_incremented(self):
        """Test if __nb_objects is incremented when an instance is created"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(type(b2)._Base__nb_objects, 2)


if __name__ == '__main__':
    unittest.main()
