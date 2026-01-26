#!/usr/bin/python3
"""
0-lookup module
Contains a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: List of attribute and method names.
    """
    return dir(obj)
