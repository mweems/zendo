from koan import Koan, SecularKoan, ExampleKoan
from rule import Rule
from random import randint
import copy

class Game(object):

	def __init__(self, diff, size, rule=None):
		self.diff = int(diff)
		size = int(size)
		if not rule:
			self.rule = Rule(self.diff)
			self.rule = self.rule.rule.split()
		else:
			self.rule = rule.split()
		attrs = self.getAttrs(self.rule, self.diff)
		self.buddhaKoan = Koan(attrs, size)
		self.secularKoan = SecularKoan(attrs, size)


	def getAttrs(self, rule, diff):
		attrs = []

		if diff == 1:
			attr = rule[3]
		elif diff == 2:
			attr = [rule[3], rule[4]]
		count = int(rule[2])
		while count > 0:
			attrs.append(attr)
			count -= 1

		return attrs


	def createUserKoan(self, attrs, size):
		self.userKoan = Koan(attrs, size)

	def checkKoan(self, userKoan, gameKoan):
		if len(userKoan.attrs) < len(gameKoan.attrs):
			print('here')
			return False
		count = 0
		for attr in gameKoan.attrs:
			if type(attr) == list:
				if attr in userKoan.attrs:
					userKoan.attrs.remove(attr)
					count += 1
					break
			else:
				for uAttr in userKoan.attrs:
					if attr in uAttr:
						userKoan.attrs.remove(uAttr)
						count += 1
						break

		if count < len(gameKoan.attrs):
			return False
		return True


	def checkRule(self, userRule):
		gameRule = (' ').join(self.rule)
		rule = userRule.split(' ')
		if 'none' in rule:
			rule.remove('none')
		userRule = (' ').join(rule)
		if gameRule == userRule:
			return True

		attrs = self.getAttrs(rule, self.diff)

		self.exampleKoan = ExampleKoan(attrs, copy.copy(self.buddhaKoan))
		return False





