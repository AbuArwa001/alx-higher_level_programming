#!/usr/bin/python3
"""Base module for shapes"""
import json
import csv


class Base:
    """Class for shapes base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def id(self):
        """Getter for `id`

        Returns:
            __id (int): unique identifer for each instance of cls

        """
        return self.__id

    @id.setter
    def id(self, value):
        """Args:
            value (int): number to be assigned as id

        Attributes:
            __id (int): unique identifer for each instance of cls

        Raises:
            ValueError: if `id` arg is 0, negative, or already assigned.

        """
        if value < 1:
            raise ValueError('id must be positive')
        self.__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries:

        Returns:
            returns the JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves list of sicts/objects  to file
        Args:
            list_objs:

        Returns:
            None
        """
        from models.square import Square
        if cls is Square:
            file_name = 'Square.json'
        else:
            file_name = 'Rectangle.json'
        if not list_objs:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write("[]")
            return
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        jstring = cls.to_json_string(list_dicts)

        with open(file_name, 'w', encoding='utf-8') as f:
            if not list_objs:
                f.write("")
            else:
                f.write(jstring)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts Json string to object
        Args:
            json_string:
                    is a string representing a list of dictionaries
        Returns:
            Returns an Object
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: Keyword arguments
                representing the attributes.

        Returns:
            An instance with all attributes already set.
        """
        from models.rectangle import Rectangle

        instance = Rectangle(1, 2, 0, 0, None)
        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        """
        Loads list from file.

        Args:

        Returns:
            Lists of dictionaries
        """
        from models.square import Square
        file_name = 'Square.json' if cls is Square else 'Rectangle.json'

        with open(file_name, 'r', encoding='utf-8') as f:
            txt = f.read()

        key = 'id'
        list_objs = cls.from_json_string(txt)

        list_dicts = [cls.create(**obj) for obj in list_objs]

        return list_dicts

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves list of dicts/objects to a CSV file.

        Args:
            list_objs: List of objects to be saved.

        Returns:
            None
        """
        from models.square import Square
        from models.rectangle import Rectangle

        if cls is Square:
            file_name = 'Square.csv'
            fieldnames = ["id", "x", "y", "size"]
        else:
            # cls.__class__ = Rectangle
            file_name = 'Rectangle.csv'
            fieldnames = ["id", "x", "y", "width", "height"]

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            shape_writer = csv.writer(file, delimiter=',', quotechar='"',
                                      quoting=csv.QUOTE_MINIMAL)

            # Writing headers of CSV file
            shape_writer.writerow(fieldnames)

            for item in list_dicts:
                if cls is Square:
                    # For Square, only write "id", "x", "y", and "size"
                    shape_writer.writerow([item['id'], item['x'],
                                           item['y'], item['size']])
                else:
                    # For Rectangle, write all fields
                    shape_writer.writerow(item.values())

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads data from a CSV file and returns a list of dictionaries.

        Returns:
            List of dictionaries.
        """
        from models.square import Square
        from models.rectangle import Rectangle

        if cls is Square:
            file_name = 'Square.csv'
            fieldnames = ("id", "x", "y", "size")
        else:
            file_name = 'Rectangle.csv'
            fieldnames = ("id", "x", "y", "width", "height")

        lists = []

        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames)

            # Skip the header row
            next(reader, None)

            for row in reader:
                # Convert string values to appropriate types
                # (int for 'id', 'x', 'y', 'size', 'width', 'height')
                converted_row = {key: int(value) for key, value in row.items()}
                # print(converted_row)
                # Create instances based on class type
                instance = cls.create(**converted_row)
                lists.append(instance)

        return lists
