is_even = lambda x: True if x % 2 == 0 else False

def conditional_print(func):
	def printer(x):
		if func(x):
			print(x)
			
	return printer
	
print_evens = conditional_print(is_even)