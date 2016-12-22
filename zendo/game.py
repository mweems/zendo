from zendo.shape import Shape
from zendo.parser import RuleParser
from random import randint
from enum import Enum

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
		colors = ('red', 'blue', 'green', 'yellow')
		rd = randint(0, num)
		while num > 0:
			shape = Shape(color=colors[rd])
			shapes.append(shape)
			num-=1
		return shapes

	def choose_rule(self):
		return 'must contain 1 blue'