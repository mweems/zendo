class Piece(object):
	colors = ['red', 'yellow', 'blue', 'green']
	sizes = ['large', 'medium', 'small']

	def __init__(self, color=None, size=None):
		self.color = color
		self.size = size

	def setColor(self, color):
		self.color = color

	def setSize(self, size):
		self.size = size
