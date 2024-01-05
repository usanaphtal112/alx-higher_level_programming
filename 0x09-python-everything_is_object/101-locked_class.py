#!/usr/bin/python3
"""restricted attribute assignment using __slots__."""


class LockedClass:
    """
    A class with restricted attribute assignment using __slots__.
    first_name (str): A slot for storing the first name.
    """
    __slots__ = ["first_name"]
