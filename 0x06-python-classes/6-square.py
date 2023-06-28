#!/usr/bin/python3
"""Classes: Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes a new square"""
        self.size = size
        self.position = position

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """retreive private attribute size"""
        return self.__size

    @property
    def position(self):
        """retreive private attribute position"""
        return self.__position

    @size.setter
    def size(self, value):
        """setting private attribute size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setting private attribute position"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints in stdout the square with the char #"""
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
