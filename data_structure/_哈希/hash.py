# coding=gbk
"""
	哈希
		- 是将任一长度的输入，通过散列算法变换成固定长度的输出
	
	哈希表
		- 根据键码值访问的数据结构
		  通过把键码值映射表中一个位置来访问记录，以加快查找速度（映射函数：散列函数，存放记录的数据：散列表）
		- 查找时间期望 O(1)
		- 处理冲突
			* 开放寻址法
				H = (hash(k) + di) MOD m, i=1,2,3...k(k<=m-1)    [hash(k):散列函数，di：增量序列]
				1. 线性探测再散列： di = 1,2,3...m-1
				2. 平方探测再散列： di = 1^2, -1^2, ...+-(k)^2 (k<=m/2)
				3. 随机探测再散列： di = 伪随机数
			* 再散列法
			* 链地址法
			* 简历公共溢出区
			
	摘要算法
		- MD5
		- SHA

		- 应用
			* 文件校验
			* 数字前面
"""

class hashtable1(object):
	def __init__(self):
		self.items = []

	def put(self, k, v):
		self.items.append((k, v))

	def get(self, k):
		for key, value in self.items:
			if (k==key):
				return value 


class hashtable2(object):
	# 直接定址法（浪费空间)
	def __init__(self):
		self.items = [None] * 100 

	def hash(self, a):
		return a*1+1 

	def put(self, k, v):
		self.items[self.hash(k)] = v 

	def get(self, k):
		hashcode = self.hash(k)
		return self.items[hashcode]


class hashtable3(object):
	# 开放地址法（线性探测）
	def __init__(self):
		self.capacity = 10 
		self.hash_table = [[None, None] for i in range(self.capacity)]
		self.num = 0 
		self.load_factor = 0.75

	def hash(self, k, i):
		h_value = (k+i) % self.capacity
		if self.hash_table[h_value][0] == k:
			return h_value 
		if self.hash_table[h_value][0] != None:
			i += 1 
			h_value = self.hash(k, i)
		return h_value 

	def resize(self):
		self.capacity = self.num * 2 
		temp = self.hash_table[:]
		self.hash_table = [[None, None] for i in range(self.capacity)]
		for i in temp:
			if (i[0] != None):
				hash_v = self.hash(i[0], 0)
				self.hash_table[hash_v][0] = i[0]
				self.hash_table[hash_v][1] = i[1]

	def put(self, k, v):
		hash_v = self.hash(k, 0)
		self.hash_table[hash_v][0] = k 
		self.hash_table[hash_v][1] = v 
		self.num = self.num + 1 
		if (self.num / len(self.hash_table) > self.load_factor):
			self.resize()

	def get(self, k):
		hash_v = self.hash(k, 0)
		return self.hash_table[hash_v]

table = hashtable3()
for i in range(1,13):
	table.put(i, i)
print(table.get(3))
print(table.hash_table)



"""
	判断素数
		- 短除法
		- 筛选法
			1、将n个数字全部放进数组，并都置为肯定状态
			2、将数组下标是偶数的数字全部置为否定状态
			3、一次遍历数组长度的平方根个数字
			4、如果当前数字处于被肯定状态，则将其背书的数字状态置为否定
"""

def find_prime(num):
	# 短除法1
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				print(num, 'is not prime num')
				print(i, '*', num//i, '=', num)
				break 
		else:
			print(num, 'is prime num')
	else:
		print(num, 'is not prime num')

# find_prime(7)


import math 

def prime_filter(num):
	# 筛选法
	primes_bool = [False, False] + [True]*(num-1)
	for i in range(3, len(primes_bool)):
		if i%2 == 0:
			primes_bool[i] = False 
	for i in range(3, int(math.sqrt(num))+1):
		if primes_bool[i] is True:
			for j in range(i+i, num+1, i):
				primes_bool[j] = False 
	primes = []
	for i, v in enumerate(primes_bool):
		if v is True:
			primes.append(i)
	return primes 


print(prime_filter(100))