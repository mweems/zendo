class Koan(object):
	
	def __init__(self, attrs):
		self.sizes = {'small': 0, 'medium': 0, 'large': 0}
		self.colors = {'red': 0, 'yellow': 0, 'green': 0, 'blue': 0}
		
		for attr in attrs:
			if attr in self.sizes:
				self.sizes[attr] += 1
			elif attr in self.colors:
				self.colors[attr] += 1
