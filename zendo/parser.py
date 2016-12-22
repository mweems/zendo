class RuleParser(object):

	def __init__(self, rule):
		self.parsed = self.parse_rule(rule)

	def parse_rule(self, rule):
		rule = rule.split()
		qty = int(rule[2])
		pr = {
			'must': [],
			'cannot': []
		}
		if rule[0] == 'must':
			pr['must'] = self.add_colors(color=rule[3], qty=qty)
		else:
			pr['cannot'] = self.add_colors(color=rule[3], qty=qty)

		return pr


	def add_colors(self, color, qty):
		colors = []
		while qty > 0:
			colors.append(color)
			qty-=1
		return colors
