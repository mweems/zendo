from nose.tools import *
from zendo.shape import Shape

def test_shape_setup():
	shape = Shape(color='red', location=[1,1])
	assert_equal('red', shape.color)
	assert_equal([1,1], shape.location)