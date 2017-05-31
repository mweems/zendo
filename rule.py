from random import randint

class Rule(object):

	rules = {
		1 : [
				[['red']],
				[['blue']],
				[['green']],
			],
		2 : [
				[['large', 'red']],
				[['medium', 'blue']],
				[['small', 'green']]
			]
	}

	def __init__(self, diff):
		ruleList = self.rules[diff]
		if len(ruleList) > 1:
			ind = randint(0, len(ruleList) - 1)
			self.rule = ruleList[ind]
		else:
			self.rule = ruleList[0]
