def sum_cubes(n):
	result = 0

	for i in range(3):
		result += (i + 1) ** n
		
	return result