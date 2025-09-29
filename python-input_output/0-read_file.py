#!/usr/bin/python3

"""
Defines a function that reads a text file (UTF8)
and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".

    Returns:
        None
    """

    with open('my_file_0.txt', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
