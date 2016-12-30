from nose.tools import *
from piece import Piece
from koan import Koan
from rule import Rule

def test_rule_returns_string_version_of_itself():
	ruleStr = 'must contain 1 red'
	rule = Rule(ruleStr)
	assert_equal(ruleStr, rule.english)