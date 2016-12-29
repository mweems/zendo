class Koan(object):

	def __init__(self, *args):
		self.pieces = []
		if args:
			for piece in args:
				self.pieces.append(piece)

	def addPiece(self, piece):
		self.pieces.append(piece)