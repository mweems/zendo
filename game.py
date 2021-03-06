from koan import Koan, SecularKoan, ExampleKoan
from rule import Rule
from random import randint
import copy

class Game(object):

	def __init__(self, diff, size, rule=None):
		self.diff = int(diff)
		size = int(size)
		if not rule:
			rule = Rule(self.diff)
			self.rule = rule.rule
		else:
			self.rule = rule
		self.buddhaKoan = Koan(self.rule, size)
		self.secularKoan = SecularKoan(self.rule, size)
		self.userList = []
		self.exampleList = []


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
		self.userList.append(copy.copy(self.userKoan))

	def checkKoan(self, userKoan, gameKoan):
		if len(userKoan.attrs) < len(gameKoan.attrs):
			print(userKoan.attrs)
			print('---------')
			print(gameKoan.attrs)
			return False
		count = 0
		pieces = copy.copy(userKoan.pieces)
		attrs = copy.copy(userKoan.attrs)
		for attr in gameKoan.attrs:
			if type(attr) == list:
				for piece in pieces:
					if piece.size in attr and piece.color in attr:
						pieces.remove(piece)
						count += 1
			else:
				for uAttr in attrs:
					if attr in uAttr:
						attrs.remove(uAttr)
						count += 1
						break

		if count < len(gameKoan.attrs):
			return False
		return True


	def checkRule(self, userRule):
		rule = userRule.split(' ')
		for attr in self.rule:
			if attr in rule:
				return True
		attrs = self.getAttrs(rule, self.diff)

		self.exampleKoan = ExampleKoan(attrs, copy.copy(self.buddhaKoan))
		self.exampleList.append(copy.copy(self.exampleKoan))
		return False





