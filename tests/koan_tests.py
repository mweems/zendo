from nose.tools import *
from koan import Koan, ReverseKoan


class TestKoan:

	def test_create_basic_koan(self):
		koan = Koan(['red'], 3)

		for p in koan.pieces:
			print("koan", p.color, p.size)

		revKoan = ReverseKoan(['red'], 3)

		for p in revKoan.pieces:
			print("revKoan", p.color, p.size)

		assert(True)