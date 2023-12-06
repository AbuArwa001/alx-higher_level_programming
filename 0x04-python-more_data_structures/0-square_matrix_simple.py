#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_list = [[j * j for j in row] for row in matrix]
    return n_list
