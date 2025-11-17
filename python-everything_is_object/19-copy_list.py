#!/usr/bin/python3
# Function that returns a copy of a list without using imports

def copy_list(my_list):
    # Using slicing ([:]) creates a new list with the same elements
    # This ensures we return a real copy and not a reference

    return my_list[:]
