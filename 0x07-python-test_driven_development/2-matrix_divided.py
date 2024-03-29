#!/usr/bin/python3
"""
matrix divided
"""

def matrix_divided(matrix, div):
    """
    matrix is divided by div not zero, new matrix created
    """
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix(list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix(list of lists) of integers/floats")
    
    length =  len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
