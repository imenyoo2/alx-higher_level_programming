#!/usr/bin/python3
"""defines add_integer function
   a and b must be integers
   a and b will be casted to int before addition operation
   tests for this modul are in tests folder
"""


def add_integer(a, b=98):
    """
    adds 2 integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
