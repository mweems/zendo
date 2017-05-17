from nose.tools import *
from koan import Koan, SecularKoan, ExampleKoan
from game import Game


class TestGame:

	def test_check_koan(self):
		rule = 'must contain 1 red'
		game = Game(1, 3, rule)
		userKoan = Koan(['small', 'red'], 1)

		assert(game.checkKoan(userKoan, game.buddhaKoan))

	def test_check_rule(self):
		rule = 'must contain 1 red'
		game = Game(1, 3, rule)

		assert(game.checkRule(rule))

	def test_example_koan(self):
		rule = 'must contain 1 red'
		game = Game(1, 3, rule)

		assert_false(game.checkRule('must contain 1 small'))

		red = 0
		small = 0

		for piece in game.exampleKoan.pieces:
			if piece.color == 'red':
				red += 1

			if piece.size == 'small':
				small += 1

		assert_equal(small, 0)
		assert(red >= 1)
