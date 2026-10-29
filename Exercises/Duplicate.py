def duplicate(str , space):
	output = ""
	
	while len(output) + len(str) <= space:
		output += str
		
	return output