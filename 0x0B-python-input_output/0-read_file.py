#!/usr/bin/python3
"""Text file-reading function."""


def read_file(filename=""):
    """
    Read and print the contents of a file.

    Args:
        filename (str): Name of the file to be read.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
        UnicodeDecodeError: If the file is not encoded in UTF-8.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
