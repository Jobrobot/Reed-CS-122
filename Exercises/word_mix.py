def word_mix(word_one, word_two):
	results_list = []
	
	if len(word_one) == 0:
		return [word_two]

	if len(word_two) == 0:
		return [word_one]

			
	for last in word_mix(word_one[1:], word_two):
		mix = word_one[0] + last
		if mix not in results_list:
			results_list.append(mix)
				
	for last in word_mix(word_one, word_two[1:]):
		mix = word_two[0] + last
		if mix not in results_list:
			results_list.append(mix)
			
	return results_list