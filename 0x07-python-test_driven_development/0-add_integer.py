#!/usr/bin/python3
"""an integer addition function."""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.

    Parameters:
    - a (int or float): The first number to be added.
    - b (int or float, optional): The second number added. Defaults to 98.

    Raises:
    - TypeError: If either 'a' or 'b' is not an integer or float.

    Returns:
    - int: The sum of 'a' and 'b' after converting them to integers.
    """
    
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
