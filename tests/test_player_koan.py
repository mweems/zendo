from nose.tools import *
from zendo.player_koans import PlayerKoan
from zendo.shape import Shape

def test_create_simple_Koan():
	pk = PlayerKoan()
	s1 = Shape(color='red')
	s2 = Shape(color='yellow')
	s3 = Shape(color='blue')
	pk.make_guess(s1, s2, s3)
	assert_equal(3, len(pk.koan))