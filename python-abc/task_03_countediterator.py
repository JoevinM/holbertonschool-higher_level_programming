#!/usr/bin/env python3
"""
This module defines the CountedIterator class, which extends Python's iterator
protocol to keep track of how many items have been iterated.
"""


class CountedIterator:
    """
    Custom iterator that counts the number of items retrieved.
    """

    def __init__(self, iterable):
        """
        Initialize with an iterable.

        Args:
            iterable (iterable): Any Python iterable (list, tuple, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator, incrementing the counter.

        Raises:
            StopIteration: When no more items are available.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated so far.

        Returns:
            int: The iteration count.
        """
        return self.count
