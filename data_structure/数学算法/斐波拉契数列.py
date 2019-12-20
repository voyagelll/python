"""
	递归实现
"""
def fib(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fib(n-1) + fib(n-2)
	else:
		print(False)


# print(fib(5))



"""
	循环
"""
def fib2(n):
	a, b = 1, 1
	l = []
	for _ in range(n):
		l.append(a)
		a, b = b, a+b
	return l


print(fib2(5))

