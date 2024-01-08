#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Define unittests for the max_integer function.

    This class contains various test cases to ensure the
    correct behavior of the max_integer function
    when provided with different types of input lists.

    Test Cases:
    - test_ordered_list: Tests when the input list is ordered.
    - test_unordered_list: Tests when the input list is unordered.
    - test_max_at_beginning: Tests when the maximum value is at the beginning
    - test_empty_list: Tests when the input list is empty.
    - test_one_element_list: Tests when the input list contains only one.
    - test_floats: Tests when the input list contains only float values.
    - test_ints_and_floats: Tests when the input list contains.
    - test_string: Tests when the input is a string.
    - test_list_of_strings: Tests when the input is a list of strings.
    - test_empty_string: Tests when the input is an empty string.
    """

    def test_ordered_list(self):
        """
        Test max_integer with an ordered list.

        The function should correctly return the maximum.
        """
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """
        Test max_integer with an unordered list.

        The function should correctly return the maximum.
        """
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """
        Test max_integer with a list where the maximum value.

        The function should correctly return the maximum value in the list.
        """
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """
        Test max_integer with an empty list.

        The function should return None for an empty list.
        """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """
        Test max_integer with a list containing only one element.

        The function should return the single element as the maximum value.
        """
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """
        Test max_integer with a list containing only float values.

        The function should correctly return the maximum float value.
        """
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """
        Test max_integer with a list containing both integers and floats.

        The function should correctly return the maximum value.
        """
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """
        Test max_integer with a string input.

        The function should correctly return the maximum character.
        """
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """
        Test max_integer with a list of strings.

        The function should correctly return the maximum string.
        """
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """
        Test max_integer with an empty string.

        The function should return None for an empty string input.
        """
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
