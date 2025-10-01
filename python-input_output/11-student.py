#!/usr/bin/python3
"""
Defines a Student class with serialization and deserialization.
"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names
            (strings) to include.
            If None or not a valid list of strings,
            all attributes are returned.

        Returns:
            dict: Dictionary of requested attributes or all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.

        Args:
            json (dict): Dictionary with new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
