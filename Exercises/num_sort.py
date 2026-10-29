def num_sort(list):
	
	for i in range(len(list)):
		for j in range(0, len(list) - i - 1):
			if list[j] > list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]
	return list



x = [8, 1 ,2, 9, 7, 3, 4, 6, 5, 10]
print(num_sort(x))