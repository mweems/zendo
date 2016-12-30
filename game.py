from piece import Piece
from koan import Koan
from color_rules import SingleColorRule, SingleSizeRule, CantColorRule

class Game(object):

# choose random rule
# create rule object
# create buddha koan
# create secular koan
# check player koan

	def __init__(self, type):
		self.buddhaKoan = Koan()

		rules = {
			'one' : 'must contain 1 red',
			'two' : 'must contain 1 large',
			'three': 'must contain 1 large red',
			'four' : 'cannot contain 1 red'
		}

		self.rule = rules[type]
		rule = self.rule.split()
		if type == 'one':
			self.buddhaKoan.addPiece(self.createColorPiece(rule[3]))
			self.finishKoan()
		if type == 'two':
			self.buddhaKoan.addPiece(self.createSizePiece(rule[3]))
			self.finishKoan()
		if type == 'three':
			piece = self.createColorPiece(rule[4])
			self.buddhaKoan.addPiece(self.createSizePiece(rule[3], piece))
			self.finishKoan()
		if type == 'four':
			self.buddhaKoan.addPiece(self.createCantPiece(rule[3]))
			self.finishKoan(rule[3])

		

	def createColorPiece(self, color,  piece=None):
		colorRule = SingleColorRule(self.rule, color, piece)
		return colorRule.getPiece()

	def createSizePiece(self, size, piece=None):
		sizeRule = SingleSizeRule(self.rule, size, piece)
		return sizeRule.getPiece()

	def createCantPiece(self, color, piece=None):
		cantRule = CantColorRule(self.rule, color, piece)
		return cantRule.getPiece()

	def finishKoan(self, color=None):
		currentLen = len(self.buddhaKoan.pieces)
		if color:
			while currentLen < 3:
				piece = Piece()
				piece.removeColor(color=color)
				self.buddhaKoan.addPiece(piece)
				currentLen +=1
		else:
			while currentLen < 3:
				self.buddhaKoan.addPiece(Piece(color='rand', size='rand'))
				currentLen +=1
		for piece in self.buddhaKoan.pieces:
			if piece.color == None:
				piece.setColor('rand')
			if piece.size == None:
				piece.setSize('rand')

