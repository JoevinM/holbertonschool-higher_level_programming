#!/usr/bin/python3
"""
Defines a function is_same_class that checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Args:
        obj: Any Python object.
        a_class: The class to compare the object against.

    Returns:
        True if obj is exactly an instance of a_class
        (not an inherited subclass).
        False otherwise.
    """

    return type(obj) is a_class
