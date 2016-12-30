from nose.tools import *
from piece import Piece
from koan import Koan


class TestKoan:

	def test_adding_piece_to_koan(self):
		piece = Piece('red', 'large')
		koan = Koan()
		koan.addPiece(piece)
		assert_equal(1, len(koan.pieces))
		koan.addPiece(piece)
		assert_equal(2, len(koan.pieces))
	
	def test_adding_multiple_pieces_to_koan(self):
		p1 = Piece('yellow', 'large')
		p2 = Piece('blue', 'medium')
		p3 = Piece('green', 'small')
		koan = Koan(p1, p2, p3)
		assert_equal(3, len(koan.pieces))