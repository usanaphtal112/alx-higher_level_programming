#!/usr/bin/python3
"""Name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string containing the first and last name.

    Parameters:
    - first_name (str): The first name.
    - last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
    - TypeError: If first_name or last_name is not a string.

    Returns:
    - None: This function does not return a value; prints the formatted string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
