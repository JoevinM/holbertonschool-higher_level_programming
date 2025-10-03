#!/usr/bin/python3


"""
Module that provides functions for JSON serialization
and deserialization to and from a file.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python object and save it to a JSON file.

    Args:
        data (object): The Python object to serialize (e.g., dict, list).
        filename (str): The name of the file where the data will be saved.
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON content from a file and deserialize it into a Python object.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The deserialized Python object (dict, list, etc.).
    """
    data = {}
    with open(filename, "r") as f:
        data = json.load(f)
    return data
