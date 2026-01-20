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
    # Check div first
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check matrix type
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
