class complex:
	def __init__(self, r, i):
		self.r = r
		self.i = i
	def __str__(self):
		return str(self.r)+"+i"+str(self.i)
	def __add__(self, c):
		print(self)
		return complex(self.r+c.r, self.i+c.i)

