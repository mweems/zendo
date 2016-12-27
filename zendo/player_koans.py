from zendo.shape import Shape

class PlayerKoan(object):

	def __init__(self):
		self.koan = []

	def make_guess(self, *shapes):
		for shape in shapes:
			self.koan.append(Shape(shape.color, shape.size))
