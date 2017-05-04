from random import randint

class Koan(object):
	
	def __init__(self, attrs, quantity):
		self.sizes = {'small': 0, 'medium': 0, 'large': 0}
		self.colors = {'red': 0, 'yellow': 0, 'green': 0, 'blue': 0}
		self.attrs = attrs
		self.pieces = []
		needed = 0
		if type(attrs[0]) == list:
			for attr in attrs:
				size = attr[0]
				color = attr[1]
				if size in self.sizes:
					self.sizes[size] += 1
				if color in self.colors:
					self.colors[color] += 1
				self.pieces.append(Piece(size=size, color=color))
			if quantity > len(self.pieces):
				needed = quantity - len(self.pieces)
			self.createPiece({}, {}, needed)

		else:
			for attr in attrs:
				if attr in self.sizes:
					self.sizes[attr] += 1
				elif attr in self.colors:
					self.colors[attr] += 1

			self.createPiece(self.sizes.copy(), self.colors.copy(), quantity)

		self.fillPieces()

	def createPiece(self, sizes, colors, quantitiy):		

		while quantitiy > 0:
			piece = Piece()
			for s in sizes:
				if sizes[s] > 0:
					piece.setSize(s)
					sizes[s] -= 1
			for c in colors:
				if colors[c] > 0:
					piece.setColor(c)
					colors[c] -= 1
			self.pieces.append(piece)
			quantitiy -= 1

	def fillPieces(self):
		for p in self.pieces:
			if not p.size:
				p.setRandSize()
			if not p.color:
				p.setRandColor()

class SecularKoan(object):

	def __init__(self, attrs, quantitiy):
		sizes = ['small', 'medium', 'large']
		colors = ['red', 'yellow', 'green', 'blue']
		self.pieces = []
		self.no = []

		if type(attrs) == list:
			for attr in attrs:
				piece = Piece(size=attr[0], color=attr[1])
				self.no.append(piece)
		else:

			for attr in attrs:
				if attr in sizes:
					sizes.remove(attr)
				if attr in colors:
					colors.remove(attr)
		self.setRandomPieces(sizes, colors, quantitiy)

	def setRandomPieces(self, sizes, colors, quantitiy):
		while quantitiy > 0:
			p = Piece()
			p.setRandSize(sizes)
			p.setRandColor(colors)
			self.pieces.append(p)
			quantitiy -= 1
		for p in self.no:
			for piece in self.pieces:
				if p.size == piece.size and p.color == piece.color:
					self.pieces.remove(piece)
					quantitiy += 1
		if quantitiy > 0:
			self.setRandomPieces(sizes, colors, quantitiy)

	

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

