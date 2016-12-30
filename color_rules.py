from rule import Rule
from piece import Piece


class SingleColorRule(Rule):

	def __init__(self, ruleStr, color):
		Rule.__init__(self, ruleStr)
		self.color = color

	def getPiece(self):
		return Piece(color=self.color)