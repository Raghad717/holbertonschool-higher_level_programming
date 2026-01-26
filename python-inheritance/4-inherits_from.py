#!/usr/bin/python3
"""
4-inherits_from module
Contains a function that checks if an object is an instance of
a subclass of a specified class (directly or indirectly).
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    from a_class (excluding obj being directly of a_class),
    otherwise False.
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
