from nose.tools import *
from game import Game

class TestGame:

	def test_game_creates_koan(self):
		game = Game('color')
		koan = game.buddhaKoan
		assert_equal(3, len(game.buddhaKoan.pieces))