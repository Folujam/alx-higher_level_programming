#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_as_strings = []
        for elem in row:
            row_as_strings.append("{:d}".format(elem))
        print(" ".join(row_as_strings))


#
'''
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in row:
            print(" ".join("{:d}".format(elem) for elem in row))
'''
