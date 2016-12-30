from random import randint

class Piece(object):

	def __init__(self, color=None, size=None):
		colorOps = ['red', 'yellow', 'blue', 'green']
		sizeOps = ['large', 'medium', 'small']
		if color == 'rand':
			color = colorOps[randint(0,3)]
		if size == 'rand':
			size = sizeOps[randint(0,2)]
		self.color = color if color in colorOps else None
		self.size = size if size in sizeOps else None

	def setColor(self, color):
		self.color = color

	def setSize(self, size):
		self.size = size
