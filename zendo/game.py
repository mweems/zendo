from zendo.shape import Shape
from zendo.parser import RuleParser
from random import randint
from enum import Enum

class Game(object):

	def __init__(self, size, rule=None):
		rule = rule
		if not rule:
			rule = self.choose_rule()
		rp = RuleParser(rule)
		self.rule = rp.parsed
		self.shapes = self.create_shapes(size, self.rule)

	def create_shapes(self, num, rule):
		shapes = []
		colors = ['red', 'blue', 'green', 'yellow']
		mustLen = len(rule.get('must'))
		notLen = len(rule.get('cannot'))
		num -= (mustLen)
		if(mustLen > 0):
			while mustLen > 0:
				shapes.append(Shape(color=rule.get('must')[0]))
				mustLen-=1
		if(notLen > 0):
			colors.remove(rule.get('cannot')[0])
			num-=1
		rd = randint(0, num)
		while num > 0:
			shape = Shape(color=colors[rd])
			shapes.append(shape)
			num-=1
		return shapes

	def choose_rule(self):
		return 'must contain 1 blue'