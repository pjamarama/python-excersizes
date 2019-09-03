class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
	def __repr__(self):
		return f"Human's name is {self.first} {self.last}"
	def __len__(self):
		return self.age
	def __add__(self, other_parent):
		if isinstance(self, Human):
			return Human(first='Newborn', last=self.last, age=0)
		raise TypeError('You cannot add that!')

a = Human('Alexey', 'Grokhotov', 35)
print(a)
print(a.age)