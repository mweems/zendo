from game import Game

diff = input('Enter a number from 1 to 2: ')
size = input('Enter a number from 3 to 6: ')

game = Game(diff, size)
print(game.rule.rule)

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

ans = 'yes'
attrList = []


def ask(ans):
	if ans == 'no':
		return
	size = input('Please enter a size, small, medium, large: ')
	color = input('Please enter a color, red, yellow, blue, green: ')
	attrList.append([size, color])
	ans = input('would you like to add another piece? yes, no: ')
	ask(ans)

ask(ans)
game.createUserKoan(attrList, len(attrList)/2 )

if game.check(game.userKoan):
	print('This Koan has the Buddha nature')
else:
	print('This Koan does not have the Buddha nature')





