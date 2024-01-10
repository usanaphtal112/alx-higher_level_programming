#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Convert a class object to a dictionary representing its attr.

    Args:
        obj: Instance of a class.

    Returns:
        dict: Dictionary representation of the class attributes.
    """
    return obj.__dict__
