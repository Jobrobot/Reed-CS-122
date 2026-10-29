
def iterate(func, times):
	
	def amount(number):
		result = number
		
		for i in range(times):
			result = func(result)
			
		return result
		
	return amount
