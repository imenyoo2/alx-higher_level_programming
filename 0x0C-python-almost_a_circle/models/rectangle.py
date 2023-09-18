#!/usr/bin/python3
"""defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter function for __width"""
        return self.__width

    @property
    def height(self):
        """getter function for __height"""
        return self.__height

    @property
    def x(self):
        """getter function for __x"""
        return self.__x

    @property
    def y(self):
        """getter function for __y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter function for __width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter function for __height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """setter function for __x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """setter function for __y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """display the Rectangle"""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """returns the string representation for Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
