#!/usr/bin/python3
"""
Defines a function that writes a Python object to a text file
using its JSON string representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a file using JSON representation.

    Args:
        my_obj: The Python object to serialize
        (e.g., dict, list, str, int, bool).
        filename (str): The name of the file where the
        JSON string will be written.

    Returns:
        None
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
