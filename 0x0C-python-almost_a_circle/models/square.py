#!/usr/bin/python3
"""defines Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the string representation for Rectangle"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
