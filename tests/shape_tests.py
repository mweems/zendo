from nose.tools import *
from zendo.shape import Shape

def test_shape_setup():
	shape = Shape('red', 'M')
	assert_equal('red', shape.color)
	assert_equal('M', shape.size)