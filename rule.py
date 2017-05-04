from random import randint

class Rule(object):

	rules = {
		1 : [
			'must contain 1 red'
			],
		2 : [
			'must contain 1 large red'
			]
	}

	def __init__(self, diff):
		ruleList = self.rules[diff]
		if len(ruleList) > 1:
			ind = randint(0, len(ruleList) - 1)
			self.rule = ruleList[ind]
		else:
			print(ruleList[0])
			self.rule = ruleList[0]
