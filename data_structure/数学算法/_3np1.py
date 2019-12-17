def ulam(n):
	l = []
	l.append(n)
	while n != 1:
		if n%2 == 1:
			n = 3*n + 1
		else:
			n /= 2
		l.append(n)
	return l


print(ulam(43))