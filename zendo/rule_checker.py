class RuleChecker(object):

	def __init__(self, koan, rule):
		self.passed = self.check_koan(koan, rule)

	def check_koan(self, koan, rule):
		must = rule['must']
		qty = len(must)
		cannot = rule['cannot']
		num = 0
		if qty > 0:
			for k in koan:
				if k.color == must[0]:
					num += 1
		if num == qty:
			return True
		else:
			return False