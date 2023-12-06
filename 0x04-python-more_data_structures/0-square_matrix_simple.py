#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) != 0:
        new_matrix = []
        for row in matrix:
            new_list = []
            for item in row:
                new_list.append(item ** 2)
            new_matrix.append(new_list)
    return (new_matrix)
