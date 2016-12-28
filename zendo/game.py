from zendo.shape import Shape
from zendo.parser import RuleParser
from random import randint
from enum import Enum


class Game(object):

	def newGame(self, size, rule):
		self.colors = ['red', 'yellow', 'green', 'blue']
		self.sizes = ['small', 'medium', 'large']

		rp = RuleParser()
		rp.parse(rule)
		
		self.rule = rp.parsed
		self.antiRule = rp.antiParsed
		self.buddhaKoan = self.create_koan(size, self.rule)
		self.secularKoan = self.create_koan(size, self.antiRule)

	def create_koan(self, num, rule):
		shapes = []
		must = rule.get('must')
		cant = rule.get('cannot')
		mustLen = len(rule.get('must'))
		notLen = len(rule.get('cannot'))
		num -= (mustLen)
		if(mustLen > 0):
			while mustLen > 0:
				shapes.append(Shape(rule.get('must')[0], 'medium'))
				mustLen-=1
		if(notLen > 0):
			self.colors.remove(cant[0])
			num-=1
		rd = randint(0, num)
		while num > 0:
			shape = Shape(self.colors[rd], 'medium')
			shapes.append(shape)
			num-=1
		return shapes