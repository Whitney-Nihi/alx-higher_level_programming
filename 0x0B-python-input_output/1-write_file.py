#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Function writes to a file and returns number of characters.

    Args:
        filename (str): The name of the file to write to.
        text (str): Text to be written to file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
