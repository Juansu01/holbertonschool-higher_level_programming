#!/usr/bin/python3
'''
This module defines a function that divides a matrix by a number.
'''


def matrix_divided(matrix, div):
    '''Function takes a matrix and a number as input, then returns
    a copy of the matrix with the result of the division.
    '''
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if len(matrix) == 1:
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix \
must have the same size")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a ma\
trix (list of lists) of integers/floats")
        for nu in row:
            if type(nu) is not int and type(nu) is not float:
                raise TypeError("matrix must be a ma\
trix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round((number / div), 2) for number in row]for row in matrix]

    return new
