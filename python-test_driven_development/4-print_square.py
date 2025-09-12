#!/usr/bin/python3

"""
Module that defines print_square function.
"""


def print_square(size):
    """
    Print a square defined by size with the "#" character.
    TypeError: if size is not an integer
    ValueError: if size is less than 0
    """
    if size == "" or size is None:
        raise TypeError("the function need a argument")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
