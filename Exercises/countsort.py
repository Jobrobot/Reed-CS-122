def countsort(list, m):
	count = [0] * m
	write_i = 0
	for i in range(len(list)):
		count[list[i]] += 1
	
	for j in range(m):
		for k in range(count[j]):
			list[write_i] = j
			write_i += 1
			
#The running time is Theta(n + m) where n is the length of the list and m is the the biggest number thats in the list + 1. So the bound is m - 1 where m goes to infinity