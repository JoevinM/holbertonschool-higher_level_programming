#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """
    Class representing a fish.
    """

    def swim(self):
        """
        Print a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message indicating the fish's habitat.
        """
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird.
    """

    def fly(self):
        """
        Print a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message indicating the bird's habitat.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish, inheriting from both Fish and Bird.
    """

    def swim(self):
        """
        Override swim method.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Override fly method.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Override habitat method.
        """
        print("The flying fish lives both in water and the sky!")
