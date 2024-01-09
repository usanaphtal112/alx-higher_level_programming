#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    Customized list class (subclass of the built-in list) with an additional.

    Methods:
    - print_sorted(): Prints the elements of the list in sorted order.

    Inherited Methods from the 'list' class:
    - All the methods available in the built-in 'list'.

    Example:
    my_list = MyList([3, 1, 4, 1, 5, 9, 2])
    my_list.print_sorted()  # Prints the elements of the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))
