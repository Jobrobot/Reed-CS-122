def selectionsort(list):
	
	for i in range(len(list)):
		smallest = i
		for j in range(i + 1, len(list)):
			if list[smallest] > list[j]:
				smallest = j
		list[i], list[smallest] = list[smallest], list[i]

#The running time of this program is theta(n^2)