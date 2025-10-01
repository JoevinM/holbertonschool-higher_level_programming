#!/usr/bin/python3
"""
Contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.

    Args:
        obj: an instance of a Class with only serializable attributes
             (list, dict, str, int, bool).

    Returns:
        dict: dictionary representation of the object
    """
    return obj.__dict__
