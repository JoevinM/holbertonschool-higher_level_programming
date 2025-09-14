#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer()."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -9, -3, -11]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_string(self):
        """max character in string (ASCII order)"""
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        """max string alphabetically"""
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

    def test_identical_elements(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)


if __name__ == '__main__':
    unittest.main()
