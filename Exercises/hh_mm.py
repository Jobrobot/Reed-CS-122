x = 1439

def hh_mm(x):
	
	hours = x // 60
	mins = x % 60
	
	if hours < 10:
		hours = "0" + str(hours)
	else:
		hours = str(hours)
		
	if mins < 10:
		mins = "0" + str(mins)
	else:
		mins = str(mins)
	
	return hours + ":" + mins
	
print(hh_mm(x))