from zendo.shape import Shape
from zendo.parser import RuleParser

class Game(object):

	def __init__(self, size, rule=None):
		self.shapes = self.create_shapes(size)
		rule = rule
		if not rule:
			rule = self.choose_rule()
		rp = RuleParser(rule)
		self.rule = rp.parsed

	def create_shapes(self, num):
		shapes = []
		while num > 0:
			shape = Shape(color='red')
			shapes.append(shape)
			num-=1
		return shapes

	def choose_rule(self):
		return 'must contain 1 blue'