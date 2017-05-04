from koan import Koan, SecularKoan
from rule import Rule
from random import randint

class Game(object):

	def __init__(self, diff, size):
		diff = int(diff)
		size = int(size)

		self.rule = Rule(diff)
		rule = self.rule.rule.split()
		
		self.attrs = []
		
		if diff == 1:
			attr = rule[3]	
		elif diff == 2:
			attr = [rule[3], rule[4]]

		count = int(rule[2])
		while count > 0:
			self.attrs.append(attr)
			count -= 1


		self.buddhaKoan = Koan(self.attrs, size)
		self.secularKoan = SecularKoan(self.attrs, size)

	def createUserKoan(self, attrs, size):
		self.userKoan = Koan(attrs, size)

	def check(self, userKoan):
		for attr in self.attrs:
			if attr not in userKoan.attrs:
				return False
		return True





