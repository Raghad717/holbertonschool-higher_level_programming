#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix
by a given number and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    matrix must be a list of lists of integers or floats.
    div must be an integer or float and cannot be zero.
    The result is a new matrix with values rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if row_length is None:
            row_length = len(row)
