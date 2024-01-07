#!/usr/bin/python3
"""
Module: 2-matrix_divided

This module provides a function matrix_divided(matrix, div)
for performing matrix division.

The function takes a matrix, which is expected to be
    a list of lists containing integers or floats.
It also takes a divisor (div), which must be
    a number (integer or float) and not equal to zero.

The matrix is divided by the divisor, and the result is
    a new matrix where each element is the quotient
of the corresponding element in the original matrix divided by the divisor.
    The result is rounded to
2 decimal places.

If the matrix or divisor is invalid, the function raises specific
    exceptions with informative error messages:
- TypeError if the matrix is not a list of lists of integers or floats
- TypeError if each row of the matrix does not have the same size
- TypeError if the divisor is not a number
- ZeroDivisionError if the divisor is zero
- TypeError if any element of the matrix is not an integer or float

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    divisor = 2
    result = matrix_divided(matrix, divisor)
    # Result:
    # [
    #    [0.5, 1.0, 1.5],
    #    [2.0, 2.5, 3.0]
    # ]
"""


def matrix_divided(matrix, div):
    """
    Function to perform matrix division.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The divisor for the matrix division.

    Returns:
        list: A new matrix where each element is
            the quotient of the corresponding element
              in the original matrix divided by the divisor.
              Rounded to 2 decimal places.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    err1 = "all elements of the matrix must be integers or floats"
    vad = (int, float)
    tst = all(isinstance(element, vad) for row in matrix for element in row)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(matrix, list):
        raise TypeError(error)
    if not tst:
        raise TypeError(err1)
    return [[round((element / div), 2) for element in row] for row in matrix]
