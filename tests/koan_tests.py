from nose.tools import *
from koan import Koan, SecularKoan, ExampleKoan
from game import Game


class TestGame:

	def test_simple_game(self):
		rule = 'must contain 1 red'
		game = Game(1, 3, rule)
		userKoan = Koan(['small', 'red'], 1)

		assert(game.checkKoan(userKoan, game.buddhaKoan))
