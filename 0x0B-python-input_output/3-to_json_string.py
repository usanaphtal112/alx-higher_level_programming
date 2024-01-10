#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.

    Args:
        my_obj: Python object to be converted to JSON.

    Returns:
        str: JSON-formatted string representing the Python object.

    Raises:
        TypeError: If the object is not serializable to JSON.
    """
    return json.dumps(my_obj)
