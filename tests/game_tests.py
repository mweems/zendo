from nose.tools import *
from zendo.game import Game

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


def test_game_follows_rule_with_all_same_color():
	rule = 'must contain 3 blue'
	initSize = 3
	num = 5
	while num > 0:
		game = Game(initSize, rule)
		for shape in game.shapes:
			assert_equal('blue', shape.color)
		num-=1
