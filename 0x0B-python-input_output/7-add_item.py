#!/usr/bin/python3
"""
Module containing add_to_list function
                    and imports to manipulate JSON FILES
"""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_to_list(filename, new_items):
    """
    Function to add list
    Args:
        filename: name of the list
        new_items: removed first item from the list

    Returns:
        Returns None

    """
    # Check if the file exists
    if os.path.exists(filename):
        try:
            # Load existing list from the file
            my_list = load_from_json_file(filename)
        except (ValueError, FileNotFoundError) as e:
            my_list = []
    else:
        my_list = []

    # Append new items to the list
    my_list.extend(new_items)

    # Save the updated list back to the file
    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    # Set the filename
    filename = "add_item.json"

    # Get command line arguments excluding the script name
    new_items = sys.argv[1:]

    # Call the add_to_list function
    add_to_list(filename, new_items)
