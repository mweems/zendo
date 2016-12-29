from nose.tools import *
from zendo.piece import Piece
from zendo.koan import Koan


def test_adding_shape_to_koan():
	piece = Piece('red', 'large')
	koan = Koan()
	koan.addPiece(piece)
	assert_equal(1, len(koan.pieces))
	koan.addPiece(piece)
	assert_equal(2, len(koan.pieces))