#!/usr/bin/python3
"""Defines an object attributes and methods lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return (dir(obj))
