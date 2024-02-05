#!/usr/bin/python3
"""Defines a sub-class MyList. that inherits from list"""


class MyList(list):
    """Public Instance Method."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
