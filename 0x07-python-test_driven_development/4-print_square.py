#!/usr/bin/python3
"""Square-printing function."""


def print_square(size):
    """
    Print a square made of '#' characters with the specified size.

    Parameters:
    - size (int): The size of the square. Must be a non-negative integer.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.

    Returns:
    - None: This function prints the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
