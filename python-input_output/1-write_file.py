#!/usr/bin/python3
"""
Defines a function that writes a string to a text file (UTF8).
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number
    of characters written.

    Args:
        filename (str): The name of the file. Defaults to "".
        text (str): The string to write into the file. Defaults to "".

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w") as f:
        f.write(text)
        return len(text)
