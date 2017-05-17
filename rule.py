from random import randint

class Rule(object):

	rules = {
		1 : [
			'must contain 1 red',
			'must contain 1 large',
			'must contain 1 blue',
			'must contain 1 yellow',
			'must contain 1 small',
			'must contain 1 medium',
			'must contain 1 large'
			],
		2 : [
			'must contain 1 large red',
			'must contain 1 medium red',
			'must contain 1 small red',
			'must contain 1 large blue',
			'must contain 1 medium blue',
			'must contain 1 small blue',
			'must contain 1 large yellow',
			'must contain 1 medium yellow',
			'must contain 1 small yellow',
			'must contain 1 large green',
			'must contain 1 medium green',
			'must contain 1 small green',
			]
	}

	def __init__(self, diff):
		ruleList = self.rules[diff]
		if len(ruleList) > 1:
			ind = randint(0, len(ruleList) - 1)
			self.rule = ruleList[ind]
		else:
			self.rule = ruleList[0]
