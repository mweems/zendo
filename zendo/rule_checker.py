#class RuleChecker(object):
#
#	def __init__(self, koan, rule):
#		self.passed = self.check_koan(koan, rule)
#
#	def check_koan(self, koan, rule):
#		must = rule['must']
#		must_qty = len(must)
#		cannot = rule['cannot']
#		cant_qty = len(cannot)
#		m_num = 0
#		c_num = 0
#		must_true = False
#		cant_true = False
#		if must_qty > 0:
#			for k in koan:
#				if k.color == must[0]:
#					m_num += 1
#		else:
#			must_true = True
#		
#		if m_num == must_qty:
#			must_true = True
#		
#		if  cant_qty > 0:
#			for k in koan:
#				if k.color == cannot[0]:
#					c_num += 1
#		else:
#			cant_true = True
#
#		if c_num < cant_qty:
#			cant_true = True
#
#		if cant_true and must_true:
#			return True
#		return False
