from rule import Rule
from piece import Piece


class SingleColorRule(Rule):

	def __init__(self, ruleStr, color):
		Rule.__init__(self, ruleStr)
		self.color = color

	def getPiece(self):
		return Piece(color=self.color)

class SingleSizeRule(Rule):

	def __init__(self, ruleStr, size):
		Rule.__init__(self, ruleStr)
		self.size = size

	def getPiece(self):
		return Piece(size=self.size)