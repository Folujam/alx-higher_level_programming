#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    In this code, the outer loop goes from 1 to n-1
    (since the first row is already defined), and the
    inner loop goes from 1 to i. The append method is
    used to add the sum of the adjacent numbers from the
    previous row to the current row. The [1] is appended
    at both ends of each row.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
