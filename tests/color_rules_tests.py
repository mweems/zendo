from nose.tools import *
from color_rules import SingleColorRule, SingleSizeRule
from piece import Piece

class TestColorRule:

	def test_single_color_rule_returns_colored_piece(self):
		ruleStr = 'must contain 1 red'
		rule = SingleColorRule(ruleStr, 'red')
		piece = Piece(color='red')
		rulePiece = rule.getPiece()
		assert_equal(piece.color, rulePiece.color)

class TestSizeRules:

	def test_single_size_rule_returns_sized_piece(self):
		ruleStr = 'must contain 1 large'
		rule = SingleSizeRule(ruleStr, 'large')
		piece = Piece(size='large')
		rulePiece = rule.getPiece()
		assert_equal(piece.size, rulePiece.size)