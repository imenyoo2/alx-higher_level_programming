#!/usr/bin/python3
"""Classes: Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """initializes a new square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
