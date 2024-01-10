#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a new string after each occurrence of a search string in a file.

    Args:
        filename (str): Name of the file to be modified.
        search_string (str): String to search for in each line.
        new_string (str): String to append after each occurrence.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user does not have write permissions.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
