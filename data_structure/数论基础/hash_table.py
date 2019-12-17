"""
	哈希表
	* 根据键码而进行直接访问的数据结构
	* 时间复杂度O(1),效率极高
"""

class hashTable(object):
	""" 直接定址法
		浪费空间
	"""

	def __init__(self):
		self.items = [None]*100

	def hash(self, a):
		return a*1+1

	def put(self, k, v):
		self.items[self.hash(k)] = v

	def get(self, k):
		hashcode = self.hash(k)
		return self.items[hashcode]




class hashTable2(object):
	"""
		开放地址法
	"""
	def __init__(self):
		self.hash_table = [[None,None] for i in range(10)]

	def hash(self, k, i):
		h_value = (k+i) % 10
		if self.hash_table[h_value][0] == k:
			return h_value
		if self.hash_table[h_value][0] != None:
			i = i + 1
			h_value = self.hash(k, i)
		return h_value

	def put(self, k, v):
		hash_v = self.hash(k, 0)
		self.hash_table[hash_v][0] = k
		self.hash_table[hash_v][1] = v

	def get(self, k):
		hash_v = self.hash(k, 0)
		return self.hash_table[hash_v][1]


table = hashTable2()
for i in range(9):
	table.put(i,i)
print(table.get(3))
print(table.hash_table)