#!/usr/bin/python3
"""defines class Rectangle"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """getter function for __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function for __height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """getter function for __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for __width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
