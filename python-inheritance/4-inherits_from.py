#!/usr/bin/python3
"""
Defines a function inherits_from that checks if an object
is an instance of a class that inherited (directly or indirectly)
from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a subclass of a_class
    (but not an instance of a_class itself).

    Args:
        obj: Any Python object.
        a_class: The class to compare the object against.

    Returns:
        True if obj is an instance of a subclass of a_class.
        False if obj is exactly an instance of a_class,
        or if it is not related to a_class at all.
    """
    return type(obj) is not a_class
