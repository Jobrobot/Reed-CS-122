
def make_even(list):
	
	for i in range(len(list)):
			if list[i] / 2 != int(list[i] / 2):
				list[i] -= 1
	return None