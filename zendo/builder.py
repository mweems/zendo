from zendo.shape import Shape
from random import randrange

#color_must_rule = {'must': [{'color': ['red', 1]}], 'cannot': []}

class Builder(object):

	self.koan = []

	def build(self, size, rule):
		self.colors = ['red', 'yellow', 'green', 'blue']
		self.sizes = ['small', 'medium', 'large']
		self.sRand = randrange(0, 3, 1)

		self.buddhaKoan = self.create_buddha_koan(size, rule)

	
	def create_koan(self, qty, rule):
		if len(rule['must']) > 0:
			self.create_must_shapes(rule['must'])
		if len(self.koan) < qty:
			while


	def create_must_shapes(self, must):
		for key in must:
			self.key(must[key])

	def color(self, list):
		num = list[1]
		while num > 0:
			self.koan.append(Shape(list[0], self.sizes[self.sRand]))
			num -= 1