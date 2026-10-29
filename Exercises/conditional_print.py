def conditional_print(func):
	def printer(x):
		if func(x):
			print(x)
			
	return printer