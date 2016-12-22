from nose.tools import *
from zendo.player_koans import PlayerKoan
from zendo.shape import Shape

def test_create_simple_Koan():
	pk = PlayerKoan()
	s1 = Shape('red')
	s2 = Shape('yellow')
	s3 = Shape('blue')
	pk.make_guess(s1, s2, s3)
	assert_equal(3, len(pk.koan))