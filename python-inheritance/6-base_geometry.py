#!/usr/bin/python3
"""Module 6-base_geometry
Defines class BaseGeometry with an unimplemented area method
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception since area is not implemented"""
        raise Exception("area() is not implemented")
