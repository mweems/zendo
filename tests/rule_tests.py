from nose.tools import *
from piece import Piece
from koan import Koan
from rule import Rule

class TestRule:

	def test_rule_returns_string_version_of_itself(self):
		ruleStr = 'A Koan must contain 1 red piece to have the Buddha nature'
		rule = Rule("must contain 1 red")
		assert_equal(ruleStr, rule.english)