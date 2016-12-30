from piece import Piece
from koan import Koan
from color_rules import SingleColorRule

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
			'size' : 'must contain 1 large'
		}

		self.rule = rules[type]
		if type == 'color':
			self.createColorPiece()
		if type == 'size':
			self.createSizePiece()
		self.finishKoan()

	def createColorPiece(self):
		rule = self.rule.split()
		colorRule = SingleColorRule(self.rule, rule[3])
		self.buddhaKoan.addPiece(colorRule.getPiece())

	def createSizePiece(self):
		pass

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
