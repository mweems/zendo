from nose.tools import *
from koan import Koan, SecularKoan
from game import Game


class TestKoan:

	def test_create_basic_koan(self):
		koan = Koan(['red', 'red', 'red'], 3)
		k2 = Koan(['red', 'red', 'red'], 3)
		game = Game(1, 2)
		print(koan.attrs)
		print(game.buddhaKoan.attrs)

		assert(False)