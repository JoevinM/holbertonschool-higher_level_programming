#!/usr/bin/python3
"""
This module defines the function add_integer.
The function takes two integers or floats (casts floats to ints),
and returns their sum as an integer.
"""


def add_integer(a, b=98):
    """ Adds two integers after checking their types.
    Floats are cast to integers before addition.
    Returns the sum of arguments a and b. """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
