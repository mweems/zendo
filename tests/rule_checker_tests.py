from nose.tools import *
from zendo.rule_checker import RuleChecker
from zendo.shape import Shape

def test_returns_true_when_pass_simple_must_and_passing_koan():
	koan = [Shape('red'), Shape('blue'), Shape('yellow')]
	rule = {
		'must': ['red'],
		'cannot': []
	}
	kc = RuleChecker(koan, rule)
	assert_equal(True, kc.passed)

def test_returns_false_when_passed_simple_must_and_failing_koan():
	koan = [Shape('blue'), Shape('green'), Shape('yellow')]
	rule = {
		'must': ['red'],
		'cannot': []
	}
	kc = RuleChecker(koan, rule)
	assert_equal(False, kc.passed)

def test_returns_true_when_multiple_color_koan():
	koan = [Shape('blue'), Shape('blue'), Shape('yellow')]
	rule = {
		'must': ['blue', 'blue'],
		'cannot': []
	}
	kc = RuleChecker(koan, rule)
	assert_equal(True, kc.passed)

def test_returns_false_when_less_than_qty():
	koan = [Shape('blue'), Shape('blue'), Shape('yellow')]
	rule = {
		'must': ['blue', 'blue', 'blue'],
		'cannot': []
	}
	kc = RuleChecker(koan, rule)
	assert_equal(False, kc.passed)

def test_returns_true_when_multiple_cannot():
	koan = [Shape('blue'), Shape('red'), Shape('yellow')]
	rule = {
		'must': [],
		'cannot': ['red', 'red']
	}
	kc = RuleChecker(koan, rule)
	assert_equal(True, kc.passed)

def test_returns_false_when_multiple_cannot():
	koan = [Shape('red'), Shape('red'), Shape('yellow')]
	rule = {
		'must': [],
		'cannot': ['red', 'red']
	}
	kc = RuleChecker(koan, rule)
	assert_equal(False, kc.passed)