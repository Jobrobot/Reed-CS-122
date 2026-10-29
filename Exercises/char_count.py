def char_count(string):
	counts = {}
	
	for i in range(len(string)):
		if string[i] in counts:
			counts[string[i]] = counts[string[i]] + 1
		else:
			counts[string[i]] = 1
	return counts
