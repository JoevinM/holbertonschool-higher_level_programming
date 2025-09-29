#!/usr/bin/python3
"""
Defines a function that returns the JSON representation of an object.
"""


def to_json_string(my_obj):
    """
    Return the JSON representation of a Python object (as a string).

    Args:
        my_obj: The Python object to serialize
        (e.g., dict, list, int, str, bool).

    Returns:
        str: A JSON-formatted string representation of the object.
    """

    import json

    return json.dumps(my_obj)
