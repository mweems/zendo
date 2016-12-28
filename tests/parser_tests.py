from nose.tools import *
from zendo.parser import RuleParser

rp = RuleParser()

def test_rule_parser_basic_must():
	rule = 'must contain 1 red'
	parsed = {
		'must': ['red'],
		'cannot': []
	}
	rp.parse(rule)
	assert_equal(parsed, rp.parsed)

def test_rule_parser_basic_cannot():
	rule = 'cannot contain 1 red'
	parsed = {
		'must': [],
		'cannot': ['red']
	}
	rp.parse(rule)
	assert_equal(parsed, rp.parsed)

def test_rule_parser_creates_anti_rule():
	rule = 'must contian 1 red'
	antiParsed = {
		'must': [],
		'cannot': ['red']
	}
	rp.parse(rule)
	assert_equal(antiParsed, rp.antiParsed)

def test_rule_parser_creates_parsed_must_size_rule():
	rule = 'must contain 1 large'
	parsed = {
		'must': ['large'],
		'cannot': []
	}
	rp.parse(rule)
	assert_equal(parsed, rp.parsed)

def test_rule_parser_creates_parsed_cannot_size_rule():
	rule = 'cannot contain 1 large'
	antiParsed = {
		'must': [],
		'cannot': ['large']
	}
	rp.parse(rule)
	assert_equal(antiParsed, rp.parsed)