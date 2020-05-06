"""
	搜索算法
		- 顺序搜索
			- 原理：
				从数据结构线性表的一段开始，顺序扫描
			- 适用： 适合于存储结构为顺序存储或链接存储的线性表
			- 时间复杂度：O(n)

		- 二分搜索
			- 原理：
				将给定值与中间节点比较，若大于中间节点，则在中间右侧表中继续上述操作
				若小于在中间节点左侧表中继续上述操作，直到找到对应的值或表不能再分
			- 适用：有序表
			- 时间复杂度：O(log(n))

		- 插值搜索
			- 原理：
				基于二分搜索算法，只是在取重点的时候把比例参数 1/2 修改为自适应参数，可以提高搜索效率
			- 适用：
				* 对于表较大，关键字分布比较均匀的查找表，插值搜索性能比二分搜索要好
				* 关键字分布不均匀，插值搜索效果不好
			- 时间复杂度 O(log(log(n)))
		
		- 跳跃搜索
			- 原理：基于二分搜索算法，采用固定间隔进行跳跃，知道找到一个符合目标元素的区间，
			       然后在该区间使用线性搜索，找到目标元素的确切位置
			- 适用：有序表
			- 复杂度： O(n^(1/2))

		- 快速搜索
			- 原理：快速搜索与快速排序方法相同，选择一个元素作为中点，根据中点将表分成两个部分。
				    不需要像快速排序一样两侧递归，而仅向一侧递归
			- 适用：用于查找无序列表中的第 k 各最小元素或最大元素
			- 复杂度:O(n)

		- 哈希搜索
			- 原理：如果所有的键都是整数，那么就可以使用一个简单的无序数组来实现。
			        将键作为索引，值即为其对应的值，这样就可以快速访问任意键的值
			- 适用： 一个简单无序数组就可以实现索引关系
			- 时间复杂度： O(1)

"""

# 顺序所有
def squence_search(sequence, target):
	for i in sequence:
		if i == target:
			return i 
	return None 


# 二分搜索
def binary_search(sequence, target):
	left = 0 
	right = len(sequence) - 1 
	while (left <= right):
		mid = (left+right) // 2 
		cur_item = sequence[mid]
		# print(cur_item, target)
		if cur_item == target:
			return mid 
		elif target < cur_item:
			right = mid - 1 
		else:
			left = mid + 1 
	return None 

# sequence = list(range(1, 1000))
# print(binary_search(sequence, 521))



# 三分所有（二分搜索拓展）
def ternary_search(sequence, target):
	left = 0 
	right = len(sequence) - 1 
	while left <= right:
		third1 = (right-left)//3 + left 
		third2 = (right-left)//3*2 + left 
		# print(left, third1, third2, right)
		if sequence[third1] == target:
			return third1 
		elif sequence[third2] == target:
			return third2 
		elif target < sequence[third1]:
			right = third1 - 1 
		elif target > sequence[third2]:
			left = third2 + 1 
		else:
			left = third1 + 1
			right = third2 - 1
	return None 

# print(ternary_search(sequence, 521))


# 插值搜索
def insert_search(sequence, target):
	left = 0 
	right = len(sequence) - 1 
	while left <= right:
		mid = left + ((target-sequence[left])*(right-left))//(sequence[right]-sequence[left])
		# print(left, mid, right)
		if mid < 0 or mid >= len(sequence):
			return None 
		cur_item = sequence[mid]
		if cur_item == target:
			return mid 
		elif target < cur_item:
			right = mid - 1 
		else:
			left = mid + 1 
	return None 


# print(insert_search(sequence, 520))


import math 
# 跳跃搜索
def jump_search(sequence, target):
	n = len(sequence)
	step = int(math.floor(math.sqrt(n)))
	prev = 0 
	while sequence[min(step, n) - 1] < target:
		prev = step
		step = step + int(math.floor(math.sqrt(n)))
		if prev >= n:
			return None 
	while sequence[prev] < target:
		prev = prev + 1 
		if prev == min(step, n):
			return None 
	if sequence[prev] == target:
		return prev 
	else:
		return None 

# print(jump_search(sequence, 521))


# 快速搜索
import random 

def partition(sequence, left, right, pivot_index):
	pivot_value = sequence[pivot_index]
	sequence[pivot_index], sequence[right] = sequence[right], sequence[pivot_index]
	store_index = left 
	for i in range(left, right):
		if sequence[i] < pivot_value:
			sequence[store_index], sequence[i] = sequence[i], sequence[store_index]
			store_index = store_index + 1 
	sequence[store_index], sequence[right] = sequence[right], sequence[store_index]
	return store_index 


def quick_search(sequence, left, right, k):
	if left == right:
		return sequence[left]
	pivot_index = left + random.randint(0, right-left+1)
	pivot_index = partition(sequence, left, right, pivot_index)
	# print(pivot_index)
	if k == pivot_index:
		return sequence[k]
	elif k < pivot_index:
		return quick_search(sequence, left, pivot_index-1, k)
	else:
		return quick_search(sequence, pivot_index+1, right, k)


# sequence = [12, 1, 21, 34, 25, 15, 35, 13, 45, 100, 234, 521, 345, 16, 1314]
# left = 0
# right = len(sequence)-1
# # k = int(input("Find the k'th smallest number in sequence,k="))-1
# k = 1
# value = quick_search(sequence, left, right, k)
# print("The %s 'th smallest number in sequence is : %s" % (k+1, value))



# 哈希搜索
class hashTable:
	def __init__(self, size):
		self.elem = [None for i in range(size)]
		self.count = size 

	def hash(self, key):
		return key % self.count 

	def insert_hash(self, key):
		address = self.hash(key)
		while self.elem[address]:
			address = (address+1) % self.count 
		self.elem[address] = key 

	def search_hash(self, key):
		star = address = self.hash(key)
		while self.elem[address] != key:
			address = (address+1) % self.count 
			if not self.elem[address] or address == star:
				return False 
		return True, address 


# list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
# hash_table = hashTable(12)
# for i in list_a:
# 	hash_table.insert_hash(i)
# print(hash_table.search_hash(15))
# print(hash_table.search_hash(33))