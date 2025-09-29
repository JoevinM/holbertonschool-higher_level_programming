#!/usr/bin/python3
"""
Defines a function that returns a Python object
from its JSON string representation.
"""
import json


def from_json_string(my_str):
    """
    Convert a JSON string into the corresponding Python object.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: A Python data structure (e.g., dict, list, str, int, bool)
                represented by the JSON string.
    """
    return json.loads(my_str)
