#!/usr/bin/python3
"""Classes: Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """initializes a new square"""
        self.size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """retreive private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting private attribute size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
