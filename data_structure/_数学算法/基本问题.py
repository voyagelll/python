"""
	3n+1问题
		1、输入一个正整数 n
		2、如果n=1 则结束
		3、如果n是奇数，则n=3n+1，否则n=n/2
		4、转入第2步
"""
def question(num):
	res = []
	steps = 0 
	while num!=1:
		res.append(num)
		steps += 1 
		if num%2 == 1:
			num = 3*num + 1 
		else:
			num /= 2 
	return res, steps 

# res, steps = question(7)
# print('res: ', res)
# print('steps: ', steps)



"""
	寻找最值问题
"""
def find_max(l):
	max = l[0]
	for i in l:
		if i > max:
			max = i 
	return max 

# print(find_max([2,4,9,7,19,94,5]))



"""
	最大公约数/最小公倍数
		- 欧几里得算法（辗转相除法）
		  定理：两个整数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数
		  数学表示：gcd(a, b) = gcd(b, a mod b)
"""


# 两个数的最大公约数和最小公倍数
def gcd(a, b): 
	while a%b != 0:
		r = a % b 
		a = b 
		b = r 
	return b 


def lcm(a, b):
	return a*b // gcd(a, b)


# print(gcd(20,2))
# print(lcm(20,2))


#三个数的最大公约数和最小公倍数
def three_gcd(a, b, c):
	return gcd(gcd(a, b), c)


def three_lcm(a, b, c):
	return a*b*c // three_gcd(a, b, c)


# print(three_gcd(2,7,6))
# print(three_lcm(2,7,6))



"""
	算术分析方法
		- 二分法
			对于区间[a, b] 上连续不断且 f(a)*f(b) < 0 的函数 y=f(x), 
			通过不断把函数 f(x) 的零点所在的区间一分为二，
			使区间的两个端点逐步逼近零点,进而得到零点近似值的方法
		- 牛顿法
			x1 = x0 - f(x0)/f'(x0)
"""
def f(x):
	return x**3 - 2*x - 5


# 二分法
def bisection(a, b):
	if f(a) == 0:
		return a 
	elif f(b) == 0:
		return b 
	elif f(a) * f(b) > 0:
		print("Counldn't find root in [a, b]")
		return 
	while f(a)*f(b) < 0:
		c = (a+b)/2 
		if f(c) == 0:
			return c 
		if abs(a-b) < 10**-7:
			return c
		elif f(c)*f(a) < 0:
			b = c 
		elif f(c)*f(b) < 0:
			a = c 
	return c 

# print(bisection(1, 1000))


# 牛顿法
def newton(s):
	x_n = s 
	while True:
		x_n1 = x_n - f(x_n)/f1(x_n)
		if abs(x_n - x_n1) < 10**-5:
			return x_n1 
		x_n = x_n1 

def f1(x):
	return 3*(x**2) - 2 


# print(newton(3))



"""
	斐波拉契亚数列
"""
# 递归
def fib(num):
	if num == 1:
		return 1 
	elif num == 2:
		return 1 
	elif num > 2:
		return fib(num-1) + fib(num-2)
	else:
		print(False)

l = [fib(i) for i in range(1,5)]
print(l)


# 循环
def fib(num):
	if num == 1:
		return [1]
	elif num == 2:
		return [1, 1]
	l = [1, 1]
	for i in range(num-2):
		l.append(l[-2]+l[-1])
	return l 

print(fib(3))