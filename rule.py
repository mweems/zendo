from random import randint

class Rule(object):

	rules = {
		1 : [
			'must contain 2 red',
			'must contain 2 large',
			'must contain 2 blue',
			'must contain 2 yellow',
			'must contain 2 small',
			'must contain 2 medium'
			],
		2 : [
			'must contain 1 large red',
			'must contain 1 small red',
			'must contain 1 large blue',
			'must contain 2 medium blue',
			'must contain 1 small yellow',
			'must contain 2 small green',
			'must contain 1 medium red'
			]
	}

	def __init__(self, diff):
		ruleList = self.rules[diff]
		if len(ruleList) > 1:
			ind = randint(0, len(ruleList) - 1)
			self.rule = ruleList[ind]
		else:
			self.rule = ruleList[0]
