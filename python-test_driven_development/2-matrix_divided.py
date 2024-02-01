#!/usr/bin/python3
"""
Divide a matrix
"""


def matrix_divided(matrix, div):
    """
        Parameters:
        matrix (int, float): matrix.
        div (int, float): the divisor of the matrix.

        Returns:
        float: The quotient of the matrix.

        Example:
        add(2, 3)
        5
    """
    if not all(isinstance(col, (int, float)) for row in matrix for col in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    size_row = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = matrix
    for row in range(len(matrix)):
        if size_row != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
        for col in range(len(matrix[0])):
            new_matrix[row][col] = matrix[row][col] / div
            new_matrix[row][col] = round(new_matrix[row][col], 2)
    return new_matrix
