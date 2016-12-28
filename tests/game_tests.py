from nose.tools import *
from zendo.game import Game

def test_start_game_creates_correct_number_of_starting_shapes_in_buddha_koan():
	rule = 'must contain 1 red'
	game = Game()
	print("start", game)
	game.newGame(3, rule)
	assert_equal(3, len(game.buddhaKoan))

def test_start_game_accepts_rule():
	rule = 'must contain 1 red'
	gameRule = {
		'must': ['red'],
		'cannot': []
	}
	game = Game()
	game.newGame(1, rule)
	assert_equal(gameRule, game.rule)


def test_game_follows_rule_with_all_same_color():
	rule = 'must contain 3 blue'
	game = Game()
	game.newGame(3, rule)
	for shape in game.buddhaKoan:
		assert_equal('blue', shape.color)
		
def test_game_follows_cannot_simple_rule():
	rule = 'cannot contain 1 blue'
	game = Game()
	print('second', game)
	game.newGame(3, rule)
	colors = []
	for shape in game.buddhaKoan:
		colors.append(shape.color)
	assert('blue' not in colors)

def test_game_creates_simple_non_buddha_koan():
	rule = 'must contain 1 yellow'
	game = Game()
	game.newGame(3, rule)
	colors = []
	for shape in game.secularKoan:
		colors.append(shape.color)
	assert('yellow' not in colors)

def test_game_creates_simple_size_koan():
	rule = 'must contain 1 large'
	game = Game()
	game.newGame(3, rule)
	sizes = []
	for shape in game.buddhaKoan:
		sizes.append(shape.size)
	assert('large' in sizes)