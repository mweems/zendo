from nose.tools import *
from zendo.builder import Builder

color_must_rule = {'must': [
	{'color': ['red', 1]}],
	'cannot': None}


def test_builder_creates_correct_number_of_starting_shapes_in_buddha_koan():
	builder = Builder()
	builder.build(3, color_must_rule)
	assert_equal(3, len(builder.buddhaKoan))

#def test_builder_follows_rule_with_all_same_color():
#	rule = [{'color': {'must': ['blue', 1]}}]
#	builder = Builder()
#	builder.build(3, rule)
#	for shape in builder.buddhaKoan:
#		assert_equal('blue', shape.color)
#		
#def test_builder_follows_cannot_simple_rule():
#	builder = Builder()
#	builder.build(3, color_cant_rule)
#	colors = []
#	for shape in builder.buddhaKoan:
#		colors.append(shape.color)
#	assert('red' not in colors)
#
#def test_builder_creates_simple_non_buddha_koan():
#	builder = Builder()
#	builder.build(3, color_cant_rule)
#	colors = []
#	for shape in builder.secularKoan:
#		colors.append(shape.color)
#	assert('red' not in colors)
#
#def test_builder_creates_simple_size_koan():
#	builder = Builder()
#	builder.build(3, size_must_rule)
#	sizes = []
#	for shape in builder.buddhaKoan:
#		sizes.append(shape.size)
#	assert('large' in sizes)