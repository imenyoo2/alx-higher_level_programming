#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixbuffer = []
    buffer = []
    for i in matrix:
        for j in i:
            buffer.append(j**2)
        matrixbuffer.append(buffer)
        buffer = []
    return matrixbuffer
