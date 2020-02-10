"""
	并查集
	- 并查集是一种数据结构，
	  用于处理对 N 个元素的集合划分和判断是否属于同集合的问题

	- 主要性质

	- 应用
	  1、维护无向图的连通性。 支持判断两个点是否在同一连通块内，和判断增加一条边是否会产生环
	  2、用在求解最小生成树的 Kruskal 算法里
"""

class union_find(object):
	"""
		创建 union_find 类，
		- 初始化两个字典，一个保存节点的父节点，另一个保存父节点的大小（将父节点自身设为1）
	"""
	def __init__(self, data_list):
		self.father_dict = {}
		self.size_dict = {}
		for node in data_list:
			self.father_dict[node] = node 
			self.size_dict[node] = 1 

	def find(self, node):
		# 添加查函数
		father = self.father_dict[node]
		if (node != father):
			father = self.find(father)
		self.father_dict[node] = father 
		return father  

	def is_same_set(self, node_a, node_b):
		# 判断两个节点是否是同一个父节点
		return self.find(node_a) == self.find(node_b)

	def union(self, node_a, node_b):
		# 合并两个节点
		if node_a is None or node_b is None:
			return 
		a_head = self.find(node_a)
		b_head = self.find(node_b)
		if (a_head != b_head):
			a_set_size = self.size_dict[a_head] 
			b_set_size = self.size_dict[b_head] 
			# 根据集合大小判断，尽量使小集合并入大集合
			if (a_set_size > b_set_size):
				self.father_dict[b_head] = a_head 
				self.size_dict[a_head] = a_set_size + b_set_size 
			else:
				# print(a_head, b_head)
				self.father_dict[a_head] = b_head 
				self.size_dict[b_head] = a_set_size + b_set_size 
				# print(self.father_dict[3])



# 初始 a = [1,2,3,4,5],并将其添加到并查集里
# 分别合并[1,2] [3,5] [3,1]
# 然后判断 2 5 是否为同一个集合
if __name__ == '__main__':
	a = [1,2,3,4,5]
	union_find = union_find(a)
	union_find.union(1,2)
	union_find.union(3,5)
	union_find.union(3,1)
	for i in range(5):
		print(i+1, union_find.find(i+1), end="\n")
	# print(union_find.father_dict)
	print(union_find.is_same_set(2,5))
	# print(union_find.father_dict)
	# print(union_find.size_dict)

