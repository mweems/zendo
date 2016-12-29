from nose.tools import *
from zendo.parser import RuleParser

#rp = RuleParser()
#
#def test_rule_parser_basic_must():
#	rule = 'must contain 1 red'
#	parsed = {
#		'must': {'color': ['red', 1]},
#		'cannot': None
#	}
#	rp.parse(rule, 1)
#	assert_equal(parsed, rp.parsed)
#
#def test_rule_parser_basic_cannot():
#	rule = 'cannot contain 1 red'
#	parsed = {
#		'must': None,
#		'cannot': {'color': ['red', 1]}
#	}
#	rp.parse(rule, 1)
#	assert_equal(parsed, rp.parsed)
#
#def test_rule_parser_creates_color_anti_must_rule():
#	rule = 'must contian 1 red'
#	antiParsed = {
#		'must': None,
#		'cannot': {'color': ['red', 1]}
#	}
#	rp.parse(rule, 1)
#	assert_equal(antiParsed, rp.antiParsed)
#
#def test_rule_parser_creates_color_anti_cant_rule():
#	rule = 'cannot contian 1 red'
#	antiParsed = {
#		'must': {'color': ['red', 1]},
#		'cannot': None
#	}
#	rp.parse(rule, 1)
#	assert_equal(antiParsed, rp.antiParsed)
#
#def test_rule_parser_creates_parsed_must_size_rule():
#	rule = 'must contain 1 large'
#	parsed = {
#		'must': {'size': ['large', 1]},
#		'cannot': None
#	}
#	rp.parse(rule, 2)
#	assert_equal(parsed, rp.parsed)
#
#def test_rule_parser_creates_parsed_cannot_size_rule():
#	rule = 'cannot contain 1 large'
#	antiParsed = {
#		'must': None,
#		'cannot': {'size': ['large', 1]}
#	}
#	rp.parse(rule, 2)
#	assert_equal(antiParsed, rp.parsed)
#
#def test_rule_parser_creates_antiParsed_cannot_size_rule():
#	rule = 'cannot contain 1 large'
#	antiParsed = {
#		'must': {'size': ['large', 1]},
#		'cannot': None
#	}
#	rp.parse(rule, 2)
#	assert_equal(antiParsed, rp.antiParsed)
#
#def test_rule_parser_creates_anitParsed_must_size_rule():
#	rule = 'must contain 1 large'
#	antiParsed = {
#		'must': None,
#		'cannot': {'size': ['large', 1]}
#	}
#	rp.parse(rule, 2)
#	assert_equal(antiParsed, rp.antiParsed)