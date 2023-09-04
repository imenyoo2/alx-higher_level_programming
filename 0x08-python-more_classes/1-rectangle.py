#!/usr/bin/python3
"""defines Rectangle"""

class Rectangle:
	"""defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
	
	@property
	def height(self):
		"""height getter"""
		return self.__height
	
	@height.setter
	def height(self, value):
		"""height setter"""
		if type(value) is not int:
			raise TypeError("height must be an integer")
		elif value < 0:
			raise ValueError("height must be >= 0")
		else:
			self.__height = value
	
	@property
	def width(self);
		"""width getter"""
		return self.__width
	
	@width.setter
	def width(self, value):
		"""width setter"""
		if type(value) is not int:
			raise TypeError("width must be an integer")
		elif value < 0:
			raise ValueError("width must be >= 0")
		else:
			self.__width = vlaue
