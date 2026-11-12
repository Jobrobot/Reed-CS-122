def longPalSub(s):
	string = ["#"]
	for char in s:
		string.append(char)
		string.append("#")
	
	radii = [0] * len(string)
	center = 0
	left = 0
	right = 0	
	best_center = 0
	longest = 0
	
	for i in range(len(string)):
		if i < right:
			mirror = 2 * center - i
			radii[i] = min(radii[mirror], right - i)
			
		left_i = i - radii[i] - 1
		right_i =  i + radii[i] + 1
		
		while left_i >= 0 and right_i < len(string) and string[left_i] == string[right_i]:
			radii[i] += 1
			left_i -= 1
			right_i += 1
			
		if i + radii[i] > right:
			center = i
			right = i + radii[i]
			
		if radii[i] > longest:
			best_center = i
			longest = radii[i]
			
	start = (best_center - longest) // 2
	return s[start: start + longest]	
