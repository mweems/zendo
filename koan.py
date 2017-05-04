from random import randint

class Koan(object):
	
	def __init__(self, attrs, size):
		self.sizes = {'small': 0, 'medium': 0, 'large': 0}
		self.colors = {'red': 0, 'yellow': 0, 'green': 0, 'blue': 0}
		self.numPieces = size
		self.pieces = []
		
		for attr in attrs:
			if attr in self.sizes:
				self.sizes[attr] += 1
			elif attr in self.colors:
				self.colors[attr] += 1

		self.tmpSize = self.sizes.copy()
		self.tmpColor = self.colors.copy()

		while size > 0:
			self.createPiece()
			size -= 1

		self.fillPieces()

	def createPiece(self):		
		piece = Piece()

		for s in self.tmpSize:
			if self.tmpSize[s] > 0:
				piece.setSize(s)
				self.tmpSize[s] -= 1
		for c in self.tmpColor:
			if self.tmpColor[c] > 0:
				piece.setColor(c)
				self.tmpColor[c] -= 1
		self.pieces.append(piece)

	def fillPieces(self):
		for p in self.pieces:
			if not p.size:
				p.setRandSize()
			if not p.color:
				p.setRandColor()

class SecularKoan(object):

	def __init__(self, attrs, size):
		self.sizes = ['small', 'medium', 'large']
		self.colors = ['red', 'yellow', 'green', 'blue']
		self.pieces = []


		for attr in attrs:
			if attr in self.sizes:
				self.sizes.remove(attr)
			if attr in self.colors:
				self.colors.remove(attr)

		while size > 0:
			p = Piece()
			p.setRandSize(self.sizes)
			p.setRandColor(self.colors)
			self.pieces.append(p)
			size -= 1

	

class Piece(object):

	def __init__(self, size=None, color=None):
		self.sizes = ['small', 'medium', 'large']
		self.colors = ['red', 'yellow', 'green', 'blue']
		self.setSize(size)
		self.setColor(color)

	def setSize(self, size):
		self.size = size

	def setColor(self, color):
		self.color = color

	def setRandSize(self, sizes=None):
		if not sizes:
			sizes = self.sizes

		ind = randint(0, len(sizes) - 1)
		self.setSize(sizes[ind])

	def setRandColor(self, colors=None):
		if not colors:
			colors = self.colors

		ind = randint(0, len(colors) - 1)
		self.setColor(colors[ind])

