#!/usr/bin/python3
"""Defines a function that appends a string to a file."""


def append_write(filename="", text=""):
    """Function appends string to end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): Text to be appended to file.
    Returns:
        The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
