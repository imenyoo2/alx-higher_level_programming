#!/usr/bin/python3
"""defines the function matrix_divided"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    # error msgs
    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    row_len = "Each row of the matrix must have the same size"
    div_type = "div must be a number"
    div_zero = "division by zero"

    # testing matrix type
    if type(matrix) is list:
        for elem in matrix:
            if type(elem) is not list:
                raise TypeError(type_msg)
            else:
                for i in elem:
                    if type(i) is not int and type(i) is not float:
                        raise TypeError(type_msg)
    else:
        raise TypeError(type_msg)

    # testing matrix row len
    length = len(matrix[0])
    for elem in matrix:
        if len(elem) != length:
            raise TypeError(row_len)

    # testing type of div
    if type(div) is not int and type(div) is not float:
        raise TypeError(div_type)
    if div == 0:
        raise ZeroDivisionError(div_zero)

    # division operation
    result = []
    for elem in matrix:
        result.append([round(x / div, 2) for x in elem])

    return result
