from nose.tools import *
from zendo.parser import RuleParser

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

def test_rule_parser_creates_anti_rule():
	rule = 'must contian 1 red'
	antiParsed = {
		'must': [],
		'cannot': ['red']
	}
	rp = RuleParser(rule)
	assert_equal(antiParsed, rp.antiParsed)