from nose.tools import *
from game import Game

class TestGame:

	def test_game_creates_koan(self):
		game = Game('one')
		assert_equal(3, len(game.buddhaKoan.pieces))

	def test_game_creates_complete_pieces(self):
		game = Game('one')
		for piece in game.buddhaKoan.pieces:
			assert(piece.color is not None)
			assert(piece.size is not None)

	def test_game_follows_basic_color_rule(self):
		# using built in simple color rules for testing
		# rule is must contain 1 red
		game = Game('one')
		count = 0
		for piece in game.buddhaKoan.pieces:
			if piece.color == 'red':
				count +=1
		assert(count > 0)

	def test_game_follows_basic_size_rule(self):
		# using built in simple color rules for testing
		# rule is must contain 1 large
		game = Game('two')
		count = 0
		for piece in game.buddhaKoan.pieces:
			if piece.size == 'large':
				count +=1
		assert(count > 0)

	def test_game_follows_combo_rule(self):
		# using built in simple color rules for testing
		# rule is must contain 1 large red
		game = Game('three')
		count = 0
		for piece in game.buddhaKoan.pieces:
			if piece.size == 'large' and piece.color == 'red':
				count +=1
		assert(count > 0)

	def test_game_follows_cant_rule(self):
		# using built in simple color rules for testing
		# rule is cannot contain 1 large red
		game = Game('four')
		count = 0
		for piece in game.buddhaKoan.pieces:
			if piece.color == 'red':
				count += 1
		assert_equal(count, 0)