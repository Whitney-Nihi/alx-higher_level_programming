#!/usr/bin/python3
"""Defines a function to check if an obj is instance of the class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object.
        a_class (type): The class.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
