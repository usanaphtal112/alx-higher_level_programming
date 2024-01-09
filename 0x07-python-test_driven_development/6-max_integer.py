#!/usr/bin/python3
"""Find the max integer in a list
"""


def max_integer(list=[]):
    """
    Find the maximum integer in the given list.

    Parameters:
    - lst (list, optional): The list of integers. Defaults to None.

    Returns:
    - int or None: The maximum integer in the list, None if the list is empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
