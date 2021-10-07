#!/usr/bin/python3
"""
This is a Divide matrix module using ``matrix_divided`` function

The function returns a matrix divided by div

"""


def matrix_divided(matrix, div):

    """divides all element of the matrix by div

    Args:
        matrix:(list), matrix to divide
        div: (int), int to divide matrix by

    Raise:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TYpeError: Each row of the matrix must have the same size
        TypeERror: div must be number
        ZeroDivisionError: division by zero

    Return:
        a new matrix with all element rounded up to 2
    """
    for lst in matrix:
        if len(lst) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elmt in lst:
            if not type(elmt) in [int, float]:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = [[round(i / div, 2) for i in x] for x in matrix]
    return new_list
