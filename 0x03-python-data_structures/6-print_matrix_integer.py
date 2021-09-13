#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m_row in matrix:
        for col in range(len(m_row)):
            print(
                "{:d}".format(m_row[col]),
                end = "\n" if col == len(m_row) - 1 else " ")
