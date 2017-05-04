from koan import Koan, SecularKoan
from rule import Rule
from random import randint

class Game(object):

	def __init__(self, diff, size):
		diff = int(diff)
		size = int(size)

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

	def createUserKoan(self, attrs, size):
		self.userKoan = Koan(attrs, size)

	def check(self, buddhaKoan, userKoan):
		for size in buddhaKoan.sizes:
			if buddhaKoan.sizes[size] > userKoan.sizes[size]:
				return False
		for color in buddhaKoan.colors:
			if buddhaKoan.colors[color] > userKoan.colors[color]:
				return False
		return True





