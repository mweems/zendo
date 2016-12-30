from nose.tools import *
from color_rules import SingleColorRule
from piece import Piece

def test_single_color_rule_sets_english():
	ruleStr = 'must contain 1 red'
	rule = SingleColorRule(ruleStr, 'red')
	assert_equal(ruleStr, rule.english)

def test_single_color_rule_returns_colored_piece():
	ruleStr = 'must contain 1 red'
	rule = SingleColorRule(ruleStr, 'red')
	piece = Piece(color='red')
	rulePiece = rule.getPiece()
	assert_equal(piece.color, rulePiece.color)