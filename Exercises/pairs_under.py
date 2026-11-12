def pairs_under(n):
	result = 0
	a = 1
	
	while a <= n:
		result += n // a
		a += 1
	return result