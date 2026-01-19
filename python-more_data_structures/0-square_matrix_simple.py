#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix: 2D list of integers.

    Returns:
        A new 2D list with each value squared.
    """
    return [[x ** 2 for x in row] for row in matrix]
