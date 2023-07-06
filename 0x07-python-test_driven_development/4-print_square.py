#!/usr/bin/python3
"""defines print_square function"""


def print_square(size):
    """prints a square with the charater #"""
    # testing type of size
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # printing
    for _ in range(size):
        print("#" * size)
