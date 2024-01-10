#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): Name of the JSON file to be loaded.

    Returns:
        dict: Loaded data as a Python dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        JSONDecodeError: If the file does not contain valid JSON
    """
    with open(filename) as f:
        return json.load(f)
