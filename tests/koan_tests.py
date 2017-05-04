from nose.tools import *
from koan import Koan, SecularKoan
from game import Game


class TestKoan:

	def test_create_basic_koan(self):
		koan = Koan(['red'], 3)

		for p in koan.pieces:
			print("koan", p.color, p.size)

		secularKoan = SecularKoan(['red'], 3)

		for p in secularKoan.pieces:
			print("revKoan", p.color, p.size)

		game = Game(1, 3)

		k = game.buddhaKoan
		s = game.secularKoan

		for p in k.pieces:
			print('game buddha', p.color, p.size)

		for p in s.pieces:
			print('game secular', p.color, p.size)


		assert(True)