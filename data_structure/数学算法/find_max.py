def find_max(l):
	max = l[0]
	for i in l[1:]:
		if i > max:
			max = i 
	return max


l = [2,4,9,7,19,94,5]
print(find_max(l))