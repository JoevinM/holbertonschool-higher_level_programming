#!/usr/bin/python3
"""
Defines class MyList that inherits from list.
"""


class MyList(list):
    """Custom list class with print_sorted method."""

    def print_sorted(self):
        """
        Print the list in ascending sorted order
        without modifying the original list.
        """
        print(sorted(self))
