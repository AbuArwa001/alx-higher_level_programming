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

