#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    l = len(matrix)
    new_matrix = [[(m[i] ** 2) for i in range(l)] for m in matrix]
    return new_matrix
