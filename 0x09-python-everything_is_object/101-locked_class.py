#!/usr/bin/python3
"""
This module defines a class called LockedClass with restricted attribute assignment using __slots__.

Attributes:
    first_name (str): A slot for storing the first name of an instance of LockedClass.
"""


class LockedClass:
    """
    A class with restricted attribute assignment using __slots__.

    Attributes:
        first_name (str): A slot for storing the first name of an instance of LockedClass.
    """

    __slots__ = ["first_name"]
