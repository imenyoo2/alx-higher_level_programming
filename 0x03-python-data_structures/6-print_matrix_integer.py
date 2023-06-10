#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for i in matrix:
        print("{}".format(i[0]), end="")
        for j in i[1:]:
            print(" {}".format(j), end="")
        print()
    return
