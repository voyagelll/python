"""
	最大公约数
"""
def gcd(a, b):
	while b:
		r = a % b
		a = b
		b = r
	return a


"""
	最小公倍数
	最大公约数 * 最小公倍数 == 两个数本身的乘积
"""
def lcm(a, b):
	return a*b // gcb(a,b)




"""
	计算三个数的最大公约数：
	思路：
		先计算两个数的最大公约数，
		在计算上述两个数的最大公约数和第三个数的最大公约数
"""
def three_gcd(a, b, c):
	g1 = gcd(a, b)
	res = gcd(g1, c)
	return res
`

def three_lcm(a, b, c):
	return (a*b*c) / three_gcd(a,b,c)


print(three_gcd(3,6,9))
print(three_lcm(3,6,9))

