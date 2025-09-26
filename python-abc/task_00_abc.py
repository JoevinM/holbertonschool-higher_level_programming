#!/usr/bin/env python3

"""
Module that defines an abstract Animal class and its subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class that represents an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should return the sound of the animal.
        Must be implemented by all subclasses.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    """
    def sound(self):
        """
        Return the sound of the dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    """
    def sound(self):
        """
        Return the sound of the cat.
        """
        return "Meow"
