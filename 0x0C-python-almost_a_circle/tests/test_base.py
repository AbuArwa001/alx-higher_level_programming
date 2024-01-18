"""Unit tests for the Base class in the shapes module.
This module includes test cases for the Base class,
which is a foundational class for other shapes like Rectangle and Square.
"""

import os
import unittest


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        from models.base import Base
        """Set up method that will be called before each test case"""
        Base._Base__nb_objects = 0

    def test_instance_creation_with_id(self):
        """Test instance creation with a specified id"""
        from models.base import Base
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_instance_creation_without_id(self):
        """Test instance creation without a specified id"""
        from models.base import Base
        b = Base()
        self.assertEqual(b.id, 1)

    def test_unique_ids(self):
        """Test if unique ids are assigned to instances"""
        from models.base import Base
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_nb_objects_private_attribute(self):
        """Test if __nb_objects is a private attribute"""
        from models.base import Base
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_nb_objects_initial_value(self):
        """Test if __nb_objects is initially 0 if id is not provided"""
        from models.base import Base
        b = Base(2)
        self.assertEqual(type(b)._Base__nb_objects, 0)

    def test_nb_objects_incremented(self):
        """Test if __nb_objects is incremented when an instance is created"""
        from models.base import Base
        b1 = Base()
        b2 = Base()
        self.assertEqual(type(b2)._Base__nb_objects, 2)

    def test_to_json_string(self):
        """Test the to_json_string method"""
        from models.rectangle import Rectangle
        from models.base import Base
        r = Rectangle(1, 2, 3, 4)
        json_string = Base.to_json_string([r.to_dictionary()])
        expected_res = '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}]'
        expected_res = eval(expected_res)[0]
        actual_dict = eval(json_string)[0]
        expected_keys = sorted(expected_res.keys())
        actual_keys = sorted(actual_dict.keys())
        self.assertEqual(actual_keys, expected_keys)

    def test_from_json_string(self):
        """Test the from_json_string method"""
        from models.rectangle import Rectangle
        from models.base import Base
        json_string = '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}]'
        list_dicts = Base.from_json_string(json_string)
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(list_dicts, [r.to_dictionary()])

    def test_create(self):
        """Test the create method"""
        from models.rectangle import Rectangle
        from models.base import Base
        r_dict = {'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r = Rectangle.create(**r_dict)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.to_dictionary(), r_dict)

    def test_save_to_file(self):
        """Test the save_to_file method"""
        from models.rectangle import Rectangle
        from models.base import Base
        r = Rectangle(1, 2, 3, 4)
        Base.save_to_file([r])
        with open('Rectangle.json', 'r', encoding='utf-8') as file:
            content = file.read()
            expected_res = ('[{"id": 1, "width": 1, '
                            '"height": 2, "x": 3, "y": 4}]')
            expected_res = eval(expected_res)[0]
            actual_dict = eval(content)[0]
            expected_keys = sorted(expected_res.keys())
            actual_keys = sorted(actual_dict.keys())
            self.assertEqual(actual_keys, expected_keys)

    def test_load_from_file(self):
        """Test the load_from_file method"""
        from models.rectangle import Rectangle
        from models.base import Base
        r = Rectangle(1, 2, 3, 4)
        Base.save_to_file([r])
        list_objs = Base.load_from_file()
        self.assertEqual(len(list_objs), 1)
        self.assertIsInstance(list_objs[0], Rectangle)
        self.assertEqual(list_objs[0].to_dictionary(), r.to_dictionary())

    def tearDown(self):
        """Clean up after each test case"""
        try:
            os.remove('Rectangle.json')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
