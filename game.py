from piece import Piece
from koan import Koan
from color_rules import SingleColorRule, SingleSizeRule

class Game(object):

# choose random rule
# create rule object
# create buddha koan
# create secular koan
# check player koan

	def __init__(self, type):
		self.buddhaKoan = Koan()

		rules = {
			'color' : 'must contain 1 red',
			'size' : 'must contain 1 large',
			'both': 'must contain 1 large red'
		}

		self.rule = rules[type]
		rule = self.rule.split()
		if type == 'color':
			self.buddhaKoan.addPiece(self.createColorPiece(rule[3]))
		if type == 'size':
			self.buddhaKoan.addPiece(self.createSizePiece(rule[3]))
		if type == 'both':
			piece = self.createColorPiece(rule[4])
			self.buddhaKoan.addPiece(self.createSizePiece(rule[3], piece))

		self.finishKoan()

	def createColorPiece(self, color,  piece=None):
		colorRule = SingleColorRule(self.rule, color, piece)
		return colorRule.getPiece()

	def createSizePiece(self, size, piece=None):
		sizeRule = SingleSizeRule(self.rule, size, piece)
		return sizeRule.getPiece()

	def finishKoan(self):
		pieces = self.buddhaKoan.pieces
		for piece in pieces:
			if piece.color == None:
				piece.setColor('rand')
			if piece.size == None:
				piece.setSize('rand')
		currentLen = len(pieces)
		while currentLen < 3:
			self.buddhaKoan.addPiece(Piece(color='rand', size='rand'))
			currentLen +=1
