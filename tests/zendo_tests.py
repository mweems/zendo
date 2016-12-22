from nose.tools import *
from zendo.shape import Shape
from zendo.game import Game

def test_shape_setup():
	shape = Shape(color='red', location=[1,1])
	assert_equal('red', shape.color)
	assert_equal([1,1], shape.location)

def test_start_game_creates_correct_number_of_starting_shapes():
	game = Game(3)
	assert_equal(3, len(game.shapes))

def test_start_game_accepts_rule():
	rule = 'must contain 1 red'
	game = Game(1, rule)
	assert_equal(rule, game.rule)

def test_start_game_creates_rule():
	rule = 'must contain 1 blue'
	game = Game(1)
	assert_equal(rule, game.rule)
