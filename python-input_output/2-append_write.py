#!/usr/bin/python3
"""
Defines a function that appends a string to the end of a text file (UTF8).
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return
    the number of characters added.

    Args:
        filename (str): The name of the file. Defaults to "".
        text (str): The string to append at the end of the file.
          Defaults to "".

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
