#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    [print(" ".join("{:d}".format(i) for i in row)) for row in matrix]
