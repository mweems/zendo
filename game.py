from koan import Koan, SecularKoan
from rule import Rule
from random import randint

class Game(object):

	def __init__(self, diff, size, rule=None):
		diff = int(diff)
		size = int(size)
		if not rule:
			self.rule = Rule(diff)
			rule = self.rule.rule.split()
		else:
			self.rule = rule.split()
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

	def checkKoan(self, userKoan):
		for attr in self.attrs:
			if attr not in userKoan.attrs[0]:
				return False
		return True

	def checkRule(self, userRule):
		self.rule = ('').join(self.rule.rule)
		rule = userRule.split(' ')
		rule.remove('none')
		userRule = (' ').join(rule)
		if self.rule == userRule:
			return True

		return False





