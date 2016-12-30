from nose.tools import *
from game import Game

class TestGame:

	def test_game_creates_koan(self):
		game = Game('color')
		assert_equal(3, len(game.buddhaKoan.pieces))

	def test_game_creates_complete_pieces(self):
		game = Game('color')
		for piece in game.buddhaKoan.pieces:
			assert(piece.color is not None)
			assert(piece.size is not None)

	def test_game_follows_basic_color_rule(self):
		# using built in simple color rules for testing
		# rule is must contain 1 red
		game = Game('color')
		count = 0
		for piece in game.buddhaKoan.pieces:
			if piece.color == 'red':
				count +=1
		assert(count > 0)

	def test_game_follows_basic_size_rule(self):
		# using built in simple color rules for testing
		# rule is must contain 1 large
		game = Game('size')
		count = 0
		for piece in game.buddhaKoan.pieces:
			if piece.size == 'large':
				count +=1
		assert(count > 0)