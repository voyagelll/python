"""
	判断素数
"""

def find_prime(num):
	"""
		短除法
	"""
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				print(num, "is not prime number")
				print(i, "*", num//i, "=", num)
				break
		else:
			print(num, 'is prime number')
	else:
		print(num, 'is not prime number')


# num = int(input('Please one nu6mber:'))
# find_prime(num)



def find_prime2(num):
	import math
	"""
		筛选法
	"""
	primes_bool = [False, False] + [True] * (num-1)
	for i in range(3, len(primes_bool)):
		if i%2 == 0:
			primes_bool[i] = False
	for i in range(3, int(math.sqrt(num))+1):
		if primes_bool[i] is True:
			for j in range(i+i, num+1, i):
				primes_bool[j] = False
	prims = []
	for i, v in enumerate(primes_bool):
		if v is True:
			prims.append(i)
	return prims


print(find_prime2(100))

