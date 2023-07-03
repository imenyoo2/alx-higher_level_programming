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

    def area(self):
        """return the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * self.width + 2 * self.height

    def __str__(self):
        """return the inform string"""
        result = ""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for i in range(self.height):
                result += "#" * self.width + "\n"
        return result[:-1]

    def __repr__(self):
        """return a string representation of the rectangle to be able to
           recreate a new instance by using eval()"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """print a msg when instance is deleted"""
        print("Bye rectangle...")
