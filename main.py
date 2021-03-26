class Calc:
	#конструктор
	def __init__(self):
		self.array = []

	def add(self, arg):
		self.array.applay(arg)
		
	def addition(self):
		result = 0
		for item in self.array:
			result += item
		return result
