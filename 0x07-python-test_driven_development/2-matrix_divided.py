#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """

    if not([len(row) for row in matrix].count(len(matrix[0])) == len(matrix)):
        raise TypeError('Each row of the matrix must have the same size')

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    """
    funtion to return error in case inappropriate matrix input
    """
    def TypeError_exec():
        exec(
            'raise(TypeError(\'matrix must be a matrix (list of lists)'
            'of integers/floats\'))')
    return [[round(x / div, 2) if type(x) in [int, float]
             else TypeError_exec() for x in row] for row in matrix]
