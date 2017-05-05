from game import Game

diff = input('Enter a number from 1 to 2: ')
size = input('Enter a number from 3 to 6: ')

game = Game(diff, size)

#remove later
print(game.rule.rule)

#example koans
print("")
print('Buddha Koan')
print("")
for piece in game.buddhaKoan.pieces:
	print(piece.size, piece.color)
print("")
print("###############")
print("")
print('Secular Koan')
print("")
for piece in game.secularKoan.pieces:
	print(piece.size, piece.color)
print("")




def addPiece(ans):
	if ans == 'no':
		return
	size = input('Please enter a size, small, medium, large: ')
	color = input('Please enter a color, red, yellow, blue, green: ')
	attrList.append([size, color])
	ans = input('would you like to add another piece? yes, no: ')
	addPiece(ans)

def guessRule():
	initial = input('Please enter "a" for "must contain" or "b" for "cannot contain": ')
	quant = input('Please enter the number of pieces required to fulfill the rule: ')
	size = input('Please enter a size, small, medium, large, or none: ')
	color = input('Please enter a color, red, yellow, blue, green, or none: ')
	rule = ''
	for attr in [size, color]:
		if attr == 'none'
			attr = ''
	if initial == "a":
		rule = ("must contain %s %s %s" %(quant, size, color))
	elif initial == "b":
		rule = ("cannot contain %s %s %S" %(quant, size, color))

	if game.checkRule(rule):
		print(" ")
		print('that is correct %s is the rule' %rule)
		print(" ")
	else:
		print(" ")
		print('that is incorrect')
		print(" ")
		addPiece('yes')

ans = 'yes'
attrList = []
addPiece(ans)

#remove later
print(attrList, 'attrlist')

game.createUserKoan(attrList, len(attrList)/2 )


if game.checkKoan(game.userKoan):
	print(" ")
	print('This Koan has the Buddha nature')
	print(" ")
	
else:
	print(" ")
	print('This Koan does not have the Buddha nature')
	print(" ")








