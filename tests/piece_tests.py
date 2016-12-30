from nose.tools import *
from piece import Piece

class TestPiece:

	def test_piece_setup(self):
		piece = Piece(color='red', size='large')
		assert_equal('red', piece.color)
		assert_equal('large', piece.size)
		piece1 = Piece()
		piece1.setColor('red')
		assert_equal('red', piece1.color)
		piece1.setSize('large')
		assert_equal('large', piece1.size)
	
	def test_piece_accepts_rand(self):
		piece = Piece(color='rand', size='rand')
		assert(piece.color is not None)
		assert(piece.size is not None)
		piece1 = Piece()
		piece1.setSize('rand')
		piece1.setColor('rand')
		assert(piece1.color is not None)
		assert(piece1.size is not None)