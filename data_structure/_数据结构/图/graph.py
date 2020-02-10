"""
	无向图：
		图是由若干定点和边相互连接组成的。边由两个顶点连接，并且没有方向的图

	有向图：
		在有向图，边是单向的

	度：
		与该顶点相关联的边的条数，顶点 v 的度记作 d(v)

	图的表示方法：数组表示法、邻接表、十字链表、临界多重表

	图的遍历：深度优先，广度优先

	图的最短路径问题：
		- Dijkstra算法（一种贪婪算法），时间复杂度O(nlog(n))(使用最小堆)，不适用有负权值的边
		- Bellman-Ford 比Dijkstra算法简单同时适用于分布式系统，时间复杂度O(VE) (V为定点数，E为边数)

	并查集
		- 并查集是一种数据结构，
		  用于处理对 N 个元素的集合划分和判断是否属于同集合的问题

		- 主要性质

		- 应用
		  1、维护无向图的连通性。 支持判断两个点是否在同一连通块内，和判断增加一条边是否会产生环
		  2、用在求解最小生成树的 Kruskal 算法里
"""


"""
	图的邻接表实现
"""
class Graph(object):
	def __init__(self):
		self.nodes = []
		self.edge = {}

	def insert(self, a, b):
		if not(a in self.nodes):
			self.nodes.append(a)
			self.edge[a] = list()
		if not (b in self.nodes):
			self.nodes.append(b)
			self.edge[b] = list()
		self.edge[a].append(b)
		self.edge[b].append(a) 

	def succ(self, a):
		return self.edge[a]

	def show_nodes(self):
		return self.nodes 

	def show_edge(self):
		print(self.edge)


# graph = Graph()
# graph.insert('0', '1')
# graph.insert('0', '2')
# graph.insert('0', '3')
# graph.insert('1', '3')
# graph.insert('2', '3')
# graph.show_edge()



"""
	图的邻接矩阵实现
"""
class Graph:
	def __init__(self, vertex):
		self.vertex = vertex 
		self.graph = [[0] * vertex for i in range(vertex)]

	def insert(self, u, v):
		# 对存在连接关系的两个点，在矩阵里置1代表存在连接关系，没有连接关系则置0 
		self.graph[u-1][v-1] = 1 
		self.graph[v-1][u-1] = 1 

	def show(self):
		for i in self.graph:
			for j in i:
				print(j, end=' ')
			print(' ')


# graph = Graph(5)
# # print(graph)
# graph.insert(1,4)
# graph.insert(4,2)
# graph.insert(4,5)
# graph.insert(2,5)
# graph.insert(5,3)
# graph.show()



"""
	深度优先遍历
"""
def dfs(G, s, S=None, res=None):
	if S is None:
		S = set()
	if res is None:
		res = []
	res.append(s)
	S.add(s)
	for u in G[s]:
		if u in S:
			continue 
		S.add(u)
		dfs(G, u, S, res)
	return res 


G = {'0': ['1', '2'],
     '1': ['2', '3'],
     '2': ['3', '5'],
     '3': ['4'],
     '4': [],
     '5': []}
# print(dfs(G, '0'))


"""
	广度优先偏离
"""
def bfs(graph, start):
	explored, queue = [], [start]
	explored.append(start)
	while queue:
		v = queue.pop(0)
		for w in graph[v]:
			if w not in explored:
				explored.append(w)
				queue.append(w)
	return explored 

# print(bfs(G, '0'))



"""
	Dijkstra算法
	使用了广度优先搜索解决赋权有向图或无向图的单源最短路径问题
"""
import heapq 


def dijkstra(graph, start, end):
	heap = [(0, start)]
	visited = []
	while heap:
		print(heap)
		(cost, u) = heapq.heappop(heap)
		# print(cost, u)
		if u in visited:
			continue 
		visited.append(u)
		if u == end:
			return cost 
		for v, c in G[u]:
			if v in visited:
				continue 
			next = cost + c 
			heapq.heappush(heap, (next, v))
	return (-1, -1)


G = {'0': [['1', 2], ['2', 5]],
     '1': [['0', 2], ['3', 3], ['4', 1]],
     '2': [['0', 5], ['5', 3]],
     '3': [['1', 3]],
     '4': [['1', 1], ['5', 3]],
     '5': [['2', 3], ['4', 3]]}
shortDistance = dijkstra(G, '4', '2')
print(shortDistance)



"""
	bellman-ford算法
"""



"""
	并查集
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
