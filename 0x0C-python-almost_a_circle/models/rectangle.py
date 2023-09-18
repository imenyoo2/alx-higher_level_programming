#!/usr/bin/python3
"""defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
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
        self.__width = value

    @height.setter
    def height(self, value):
        """setter function for __height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """setter function for __x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """setter function for __y"""
        self.__y = value
