from nose.tools import *
from koan import Koan


class TestKoan:

	def test_create_basic_koan(self):
		koan = Koan(['red'])
		count = koan.colors['red']
		assert_equal(count, 1)

		koan = Koan(['large'])
		count = koan.sizes['large']
		assert_equal(count, 1)

		koan = Koan(['red', 'red'])
		count = koan.colors['red']
		assert_equal(count, 2)