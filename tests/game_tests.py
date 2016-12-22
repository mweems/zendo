from nose.tools import *
from zendo.game import Game

def test_start_game_creates_correct_number_of_starting_shapes_in_buddha_koan():
	game = Game(3)
	assert_equal(3, len(game.buddhaKoan))

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
		for shape in game.buddhaKoan:
			assert_equal('blue', shape.color)
		num-=1

def test_game_follows_cannot_simple_rule():
	rule = 'cannot contain 1 blue'
	initSize = 3
	game = Game(initSize, rule)
	colors = []
	for shape in game.buddhaKoan:
		colors.append(shape.color)
	assert('blue' not in colors)

def test_game_creates_simple_non_buddha_koan():
	rule = 'must contain 1 yellow'
	initSize = 3
	game = Game(initSize, rule)
	colors = []
	for shape in game.secularKoan:
		colors.append(shape.color)
	assert('yellow' not in colors)