from koan import Koan
from random import randint

class Game(object):

	sizes = ['small', 'medium', 'large']
	colors = ['red', 'yellow', 'green', 'blue']



	def __init__(self, diff):

		rules = {
			1: 'must contain 1 red',
			2: 'must contain 1 large',
		}

		self.rule = rules[diff]
		rule = self.rule.split()
		attrs = []
		if diff == 1 or diff == 2:
			attr = rule[3]
			count = int(rule[2])
			while count > 0:
				attrs.append(attr)
				count -= 1

		self.buddhaKoan = Koan(attrs)
		self.secularKoan = self.reverseKoan(attrs, diff)



	def reverseKoan(self, attrs, diff):
		tmpSize = self.sizes
		tmpColor = self.colors
		revAttrs = []
		for attr in attrs:
			if attr in self.sizes:
				tmpSize.remove(attr)
			elif attr in self.colors:
				tmpColor.remove(attr)

		if len(tmpSize) == len(self.sizes):
			revAttrs = self.addAttrs(tmpColor, diff)
		elif len(tmpColor) == len(self.colors):
			revAttrs = self.addAttrs(tmpSize, diff)

		return Koan(revAttrs)

	def addAttrs(self, attrs, diff):
		revAttrs = []
		while diff > 0:
			ind = randint(0, len(attrs) - 1)
			revAttrs.append(attrs[ind])
			diff -= 1
		return revAttrs


