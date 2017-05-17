from game import Game

class Zendo(object):

	def __init__(self):
		diff = input('Enter a number from 1 to 2: ')
		size = input('Enter a number from 3 to 6: ')

		self.game = Game(diff, size)

		#remove later
		print(self.game.rule)
		
		self.printKoans()
		self.addPiece('yes', [])

	def printKoans(self, userKoan=None, exampleKoan=None):
		print("")
		print('Buddha Koan')
		print("")
		for piece in self.game.buddhaKoan.pieces:
			print(piece.size, piece.color)
		print("")
		print("###############")
		print("")
		print('Secular Koan')
		print("")
		for piece in self.game.secularKoan.pieces:
			print(piece.size, piece.color)
		print("")
		if userKoan:
			print("")
			print("###############")
			print("")
			print('Your Koan')
			print("")
			for piece in userKoan.pieces:
				print(piece.size, piece.color)
			print("")
		if exampleKoan:
			print("")
			print("###############")
			print("")
			print('Example Koan')
			print("")
			for piece in exampleKoan.pieces:
				print(piece.size, piece.color)
			print("")
	
	def guessRule(self):
		initial = input('Please enter "a" for "must contain" or "b" for "cannot contain": ')
		quant = input('Please enter the number of pieces required to fulfill the rule: ')
		size = input('Please enter a size, small, medium, large, or none: ')
		color = input('Please enter a color, red, yellow, blue, green, or none: ')
		rule = ''
		for attr in [size, color]:
			if attr == 'none':
				attr = ''
		if initial == "a":
			rule = ("must contain %s %s %s" %(quant, size, color))
		elif initial == "b":
			rule = ("cannot contain %s %s %S" %(quant, size, color))
	
		if self.game.checkRule(rule):
			print(" ")
			print('that is correct %s is the rule' %rule)
			print(" ")
			return
		else:
			print(" ")
			print('that is incorrect')
			print(" ")
			self.printKoans(userKoan=self.game.userKoan, exampleKoan=self.game.exampleKoan)
			self.addPiece('yes', [])
	
	
	
	def addPiece(self, ans, attrList):
		if ans == 'no':
			self.checkKoans(attrList)
		size = input('Please enter a size, small, medium, large: ')
		color = input('Please enter a color, red, yellow, blue, green: ')
		attrList.append([size, color])
		ans = input('would you like to add another piece? yes, no: ')
		self.addPiece(ans, attrList)
	
	def checkKoans(self, attrList):
		self.game.createUserKoan(attrList, len(attrList) )
		if self.game.checkKoan(self.game.userKoan, self.game.buddhaKoan):
			print(" ")
			print('This Koan has the Buddha nature')
			print(" ")
		else:
			print(" ")
			print('This Koan does not have the Buddha nature')
			print(" ")
		
		self.printKoans(self.game.userKoan)
		guess = input('Would you like to guess the rule? y, n: ')
		if guess == 'y':
			self.guessRule()
		else:
			self.addPiece('yes', [])


if __name__ == '__main__':
	Zendo()



