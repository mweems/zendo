from nose.tools import *
from piece import Piece

def test_shape_setup():
	piece = Piece()
	piece.setColor('red')
	assert_equal('red', piece.color)
	piece.setSize('large')
	assert_equal('large', piece.size)