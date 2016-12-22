from nose.tools import *
from zendo.shape import Shape
from zendo.game import Game
from zendo.parser import RuleParser

def test_shape_setup():
	shape = Shape(color='red', location=[1,1])
	assert_equal('red', shape.color)
	assert_equal([1,1], shape.location)

def test_start_game_creates_correct_number_of_starting_shapes():
	game = Game(3)
	assert_equal(3, len(game.shapes))

def test_start_game_accepts_rule():
	rule = 'must contain 1 red'
	gameRule = {
		'must': ['red'],
		'cannot': []
	}
	game = Game(1, rule)
	assert_equal(gameRule, game.rule)

def test_start_game_creates_rule():
	rule = 'must contain 1 blue'
	gameRule = {
		'must': ['blue'],
		'cannot': []
	}
	game = Game(1)
	assert_equal(gameRule, game.rule)

def test_rule_parser_basic_must():
	rule = 'must contain 1 red'
	parsed = {
		'must': ['red'],
		'cannot': []
	}
	rp = RuleParser(rule)
	assert_equal(parsed, rp.parsed)

def test_rule_parser_basic_cannot():
	rule = 'cannot contain 1 red'
	parsed = {
		'must': [],
		'cannot': ['red']
	}
	rp = RuleParser(rule)
	assert_equal(parsed, rp.parsed)
