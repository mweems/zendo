from nose.tools import *
from game import Game


class TestGame:

	def test_game_creates_both_koans(self):
		game = Game(1)
		count = game.buddhaKoan.colors['red']
		colors = game.secularKoan.colors
		assert_equals(count, 1)
		assert_equals(colors['red'], 0)

		game = Game(2)
		count = game.buddhaKoan.sizes['large']
		sizes = game.secularKoan.sizes
		assert_equals(count, 1)
		assert_equals(sizes['large'], 0)
