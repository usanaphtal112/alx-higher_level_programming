#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Write the given text to a file.

    Args:
        filename (str): Name of the file to be written.
        text (str): Text to be written to the file.

    Returns:
        int: Number of characters written to the file.

    Raises:
        PermissionError: If the user does not have write permissions.
        UnicodeEncodeError: If the text cannot be encoded in UTF-8.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
