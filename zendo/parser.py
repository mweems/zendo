class RuleParser(object):

	def parse(self, rule):
		rule = rule.split()
		qty = int(rule[2])
		self.parsed = self.parse_rule(rule[3], qty, type=rule[0])
		self.antiParsed = self.parse_anti_rule(rule[3], qty, type=rule[0])

	def parse_rule(self, color, qty, type):
		pr = {'must':[], 'cannot': []}
		pr[type] = self.add_colors(color, qty)
		return pr

	def parse_anti_rule(self, color, qty, type):
		pr = {'must':[], 'cannot': []}
		if(type == 'must'):
			type = 'cannot'
		else:
			type = 'must'
		pr[type] = self.add_colors(color, qty)
		return pr

	def add_colors(self, color, qty):
		colors = []
		while qty > 0:
			colors.append(color)
			qty-=1
		return colors
