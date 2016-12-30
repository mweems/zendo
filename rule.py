from piece import Piece

class Rule(object):

	def __init__(self, ruleStr, piece):
		self.english = "A Koan %s piece to have the Buddha nature" % ruleStr
		self.piece = piece if piece else Piece()
