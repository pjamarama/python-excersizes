def my_for(word, func):
	it = iter(word)
	while True:
		try:
			thing = next(it)
		except StopIteration:
			# print('End of iterator')
			break
		else:
			func(thing)

def square(x):
	print(x*x)

my_for([1,2,3,4,5], square)