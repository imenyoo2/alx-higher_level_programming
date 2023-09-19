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

    @property
    def size(self):
        """getter function for size (not an attribute btw)"""
        return self.width

    @size.setter
    def size(self, value):
        """setter function for size (not an attribute btw)"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attributes of Square"""
        if len(args) != 0:
            try:
                it = iter(args)
                self.id = next(it)
                self.size = next(it)
                self.x = next(it)
                self.y = next(it)
            except StopIteration:
                return
        else:
            try:
                self.id = kwargs['id']
            except KeyError:
                pass
            try:
                self.width = kwargs['size']
            except KeyError:
                pass
            try:
                self.x = kwargs['x']
            except KeyError:
                pass
            try:
                self.y = kwargs['y']
            except KeyError:
                pass

    def to_dictionary(self):
        """returns the Dictionary representation of Square"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
