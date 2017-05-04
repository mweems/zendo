from koan import Koan, SecularKoan
from rule import Rule
from random import randint

class Game(object):

	def __init__(self, diff, size):
		self.diff = diff
		self.size = size

		rule = Rule(diff)
		rule = rule.rule.split()
		
		attrs = []
		
		if diff == 1:
			attr = rule[3]
			count = int(rule[2])
			while count > 0:
				attrs.append(attr)
				count -= 1

		self.buddhaKoan = Koan(attrs, size)
		self.secularKoan = SecularKoan(attrs, size)


