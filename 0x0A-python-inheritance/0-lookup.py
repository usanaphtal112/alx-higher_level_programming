#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Retrieves and returns a list of valid attributes

    Parameters:
    - obj: The object for which to retrieve attributes and methods.

    Returns:
    A list containing the names of attributes and methods associated
    """
    return (dir(obj))
