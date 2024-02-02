#!/usr/bin/python3
"""Defines a function that adds two integers."""


def add_integer(a, b=98):
    """Returns the addition of a and b.

    Float values must be typecasted to integers before adding.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:  
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
