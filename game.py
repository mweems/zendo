from piece import Piece
from koan import Koan
from color_rules import SingleColorRule

class Game(object):

# choose random rule
# create rule object
# create buddha koan
# create secular koan
# check player koan
	rules = {
		'color' : 'must contain 1 red',
		'size' : 'must contain 1 large'
	}

	buddhaKoan = Koan()

	def __init__(self, type):
		self.rule = rules[type]
		if type == 'color':
			createColorShape()
		if type == 'size':
			createSizeShape()
		finishKoan()

	def createColorShape(self):
		rule = self.rule.split()
		colorRule = SingleColorRule(self.rule, rule.get(3))
		buddhaKoan.addPiece(colorRule.getPiece())

	def finishKoan(self):
		currentLen = len(buddhaKoan)
		while currentLen < 3:
			buddhaKoan.append(Piece(color='rand', size='rand'))
			currentLen +=1
