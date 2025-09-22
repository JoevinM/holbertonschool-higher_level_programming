#!/usr/bin/python3
"""
Defines a function is_kind_of_class that checks if an object
is an instance of a class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or a subclass of it.

    Args:
        obj: Any Python object.
        a_class: The class to compare the object against.

    Returns:
        True if obj is an instance of a_class or of a subclass of a_class.
        False otherwise.
    """
    return isinstance(obj, a_class)
