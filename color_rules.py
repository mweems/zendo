from rule import Rule
from piece import Piece


class SingleColorRule(Rule):

	def __init__(self, ruleStr, color, piece=None):
		Rule.__init__(self, ruleStr, piece)
		self.color = color

	def getPiece(self):
		self.piece.setColor(color=self.color)
		return self.piece

class SingleSizeRule(Rule):

	def __init__(self, ruleStr, size, piece=None):
		Rule.__init__(self, ruleStr, piece)
		self.size = size

	def getPiece(self):
		self.piece.setSize(size=self.size)
		return self.piece

class CantColorRule(Rule):

	def __init__(self, ruleStr, color, piece=None):
		Rule.__init__(self, ruleStr, piece)
		self.color = color

	def getPiece(self):
		self.piece.removeColor(color=self.color)
		return self.piece