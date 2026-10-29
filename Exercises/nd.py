def nd(n):
	oned = n % 10
	answer = ""
	
	if oned == 1 or oned == 2 or oned == 3:
		if oned == 1:
			answer = str(n) + "st"
		elif oned == 2:
			answer = str(n) + "nd"
		else:
			answer = str(n) + "rd"
	else:
		answer = str(n) + "th"
		
	return answer