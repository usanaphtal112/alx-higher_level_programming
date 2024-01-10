#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string to a Python object.

    Args:
        my_str (str): JSON-formatted string to be converted.

    Returns:
        obj: Python object created from the JSON string.

    Raises:
        JSONDecodeError: If the string does not contain valid JSON.
    """
    return json.loads(my_str)
