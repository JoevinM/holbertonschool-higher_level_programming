#!/usr/bin/env python3
"""
This module defines the VerboseList class,
which extends Python's built-in list.
It overrides certain methods to print notifications whenever elements are added
or removed.
"""


class VerboseList(list):
    """
    A custom list that prints a message whenever items are added or removed.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with elements from an iterable
        and print a notification.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list
        and print a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at index (default last)
        and print a notification.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
