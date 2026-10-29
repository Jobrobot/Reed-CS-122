def sum_power2(x):

	if x == 0:
		return "1"
	prev = sum_power2(x-1)
	
	return f"({prev}+{prev})"
	