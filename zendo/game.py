from zendo.shape import Shape

class Game(object):

	def __init__(self, size, rule=None):
		self.shapes = self.create_shapes(size)
		self.rule = rule
		if not rule:
			self.rule = self.choose_rule()



	def create_shapes(self, num):
		shapes = []
		while num > 0:
			shape = Shape(color='red')
			shapes.append(shape)
			num-=1
		return shapes

	def choose_rule(self):
		return 'must contain 1 blue'