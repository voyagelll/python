"""
    图的临街表实现
"""
class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edge = {}

    def insert(self, a, b):
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edge[a] = []
        if not (b in self.nodes):
            self.nodes.append(b)
            self.edge[b] = []
        self.edge[a].append(b)
        self.edge[b].append(a)

    def succ(self, a):
        return self.edge[a]

    def show_nodes(self):
        return self.nodes

    def show_edge(self):
        return self.edge


# graph = Graph()
# graph.insert('0', '1')
# graph.insert('1', '2')
# graph.insert('2', '3')
# graph.insert('3', '0')
# print(graph.show_edge())



"""
    图的邻接矩阵实现
"""
class GraphMatrix():
    def __init__(self, v):
        self.v = v
        self.graph = [[0] * v for i in range(v)]

    def insert(self, u, v):
        self.graph[u-1][v-1] = 1
        self.graph[v-1][u-1] = 1

    def show(self):
        for i in self.graph:
            for j in i:
                print(j, end=" ")
            print(" ")


# graph = GraphMatrix(5)
# graph.insert(1,0)
# graph.insert(1,1)
# graph.insert(1,2)
# graph.insert(1,3)
# graph.show()


"""
    深度优先
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


# G = {'0': ['1', '2'],
#      '1': ['2', '3'],
#      '2': ['3', '5'],
#      '3': ['4'],
#      '4': [],
#      '5': []}
# print(dfs(G, '0'))


"""
    广度优先
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


"""
    Dijkstra算法：使用了广度优先搜索解决福泉有向图的单源最短路径问题
"""
import heapq

def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = []
    while heap:
        print(heap)
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.append(u)
        if u == end:
            return cost
        for v, c in graph[u]:
            if v in visited:
                continue
            next = cost + c
            heapq.heappush(heap, (next, v))
    return (-1, -1)

# G = {'0': [['1', 2], ['2', 5]],
#      '1': [['0', 2], ['3', 3], ['4', 1]],
#      '2': [['0', 5], ['5', 3]],
#      '3': [['1', 3]],
#      '4': [['1', 1], ['5', 3]],
#      '5': [['2', 3], ['4', 3]]}


G = {
    '0': [['1', 1], ['2', 1]],
    '1': [['3', 1]],
    '2': [['4', 3]],
    '3': [['4', 1]],
}
print(dijkstra(G, '0', '4'))




