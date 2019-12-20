"""
	二分法
	对于在区间【a,b] 上连续且f(a)*f(b) < 0 的函数 y=f(x)
	通过把f(x) 所在的零点区间一分为二，使区间两个断电逐步逼近零点
	进而得到近似零点值
"""
import time 

def fun(a):
	return a**3 - 2*a - 5


def binary_divide(a, b):
	if fun(a) == 0:
		return a
	elif fun(b) == 0:
		return b 
	elif fun(a) * fun(b) > 0:
		print('Could not find root in [a, b]')
	else:
		mid = (a + b) / 2
		while abs(fun(mid)) > 10**-7:
			if fun(mid) == 0:
				return mid
			elif fun(mid) * fun(a) < 0:
				b = mid
			else:
				a = mid
			mid = (a + b) / 2
			print(a, b, mid, fun(mid))
			time.sleep(0.1)
		return mid


# binary_divide(1, 1000)




"""
	牛顿法
	通过切线不断逼近零点
"""
def fun1(a):
	return 3*(a**2) - 2


def newton(fun, fun1, a):
	while True:
		a1 = a - fun(a)/fun1(a)
		if abs(a-a1) < 10**-5:
			return a1
		a = a1
		print(a, a1)
		time.sleep(0.1)


newton(fun, fun1, 1)
