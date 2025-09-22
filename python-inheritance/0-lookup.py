#!/usr/bin/python3
"""
This module provides a utility function to return the list of
attributes and methods of a given Python object.
"""


def lookup(obj):
    """
    Return the list of attributes and methods of an object.

    Args:
        obj: Any Python object (e.g., list, dict, str, class, instance).

    Returns:
        list: A list of attribute and method names available for the object.
    """

    return (dir(obj))
