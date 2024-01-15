#!/usr/bin/python3
"""Base module for shapes"""
import json


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
        list_dicts = [cls.to_dictionary(obj) for obj in list_objs]
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
            **dictionary: Keyword arguments representing the attributes.

        Returns:
            An instance with all attributes already set.
        """
        from models.rectangle import Rectangle

        instance = Rectangle(1, 2, 3, 4, None)
        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        from models.square import Square
        file_name = 'Square.json' if cls is Square else 'Rectangle.json'

        with open(file_name, 'r', encoding='utf-8') as f:
            txt = f.read()

        key = 'id'
        list_objs = cls.from_json_string(txt)

        list_dicts = [cls.create(**obj) for obj in list_objs]

        return list_dicts
