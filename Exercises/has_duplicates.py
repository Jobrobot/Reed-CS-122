def has_duplicates(list):

	for i in range(len(list)):
		for a in range(i + 1, len(list)):
			if list[i] == list[a]:
				return True
				
	return False
			