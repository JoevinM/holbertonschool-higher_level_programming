#!/usr/bin/python3
"""
This module defines the function say_my_name.

The function prints a formatted string with the given first name
and optional last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted full name.
    Checks that first_name and last_name are strings.
    Displays: My name is <first name> <last name>.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
