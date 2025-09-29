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
        my_obj: The Python object to serialize (e.g., dict, list, str, int, bool).
        filename (str): The name of the file where the JSON string will be written.

    Returns:
        None
    """
    # Open the file in write mode with UTF-8 encoding
    # If the file exists, its content will be overwritten
    with open(filename, "w", encoding="utf-8") as f:
        # Convert the Python object into a JSON string and write it to the file
        f.write(json.dumps(my_obj))
