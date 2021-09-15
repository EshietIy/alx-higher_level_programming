#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[(m[i] ** 2) for i in range(3)] for m in matrix]
    return new_matrix
