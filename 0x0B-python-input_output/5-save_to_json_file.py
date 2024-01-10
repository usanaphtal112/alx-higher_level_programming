#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Save Python object to a JSON file.

    Args:
        my_obj: Python object to be saved.
        filename (str): Name of the JSON file to be created.

    Returns:
        None

    Raises:
        TypeError: If the object is not serializable to JSON.
        PermissionError: If the user does not have write permissions.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
