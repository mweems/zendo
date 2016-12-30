from random import randint

class Piece(object):

	def __init__(self, color=None, size=None):
		self.colorOps = ['red', 'yellow', 'blue', 'green']
		self.sizeOps = ['large', 'medium', 'small']
		self.pipOps = {'large': 3, 'medium': 2, 'small': 1}

		self.setColor(color) 
		self.setSize(size)

	def setColor(self, color):
		if color == 'rand':
			color = self.colorOps[randint(0,3)]
		self.color = color if color in self.colorOps else None

	def setSize(self, size):
		if size == 'rand':
			size = self.sizeOps[randint(0,2)]
		self.size = size if size in self.sizeOps else None
		if size:
			self.pips = self.pipOps[size]
