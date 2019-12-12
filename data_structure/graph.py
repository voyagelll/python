"""
    图
    无向图：
        图是若干个顶点（vertices）变（edge）相互链接组成的。边仅由两个顶点连接，并且没有方向的图称为无向图
    有向图：
        有向图中，边是单向的，每条边连接的两个顶点都是一个有序对，它们的邻接性是单向的。开发过程中碰到的很多场景都是有向图。
        比如任务调度的以来关系，社交网络的任务关系等都是天然的有向图
    度：
        一个顶点的度是指与该顶点关联的边的条数，顶点V的度记作 d(V)

    图的实现：
        表示图通常有四中方法：数组表示法，邻接表，十字链表，邻接多重表
            邻接表：是图的一种链式存储结构
            十字链表：是有向图的另一种链式存储结构
            邻接多重表：是无向图的另一种链式存储结构
"""


class Graph(object):
    """
        无向图
        邻接表实现
    """
    def __init__(self):
        self.nodes = []   # 图的点集
        self.edge = {}    # 图的边集

    def insert(self, a, b):
        if not (a in self.nodes):
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


class GraphMatrix(object):
    """
        图的邻接矩阵实现
    """
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] * vertex for i in range(vertex)]

    def insert(self, u, v):
        # 对存在连接关系的两个点，在矩阵里1代表存在连接关系，0表示没有
        self.graph[u-1][v-1] = 1
        self.graph[v-1][u-1] = 1

    def show(self):
        for i in self.graph:
            for j in i:
                print(j, end=' ')
            print(' ')


if __name__ == '__main__':
    g = Graph()
    g.insert('0', '1')
    g.insert('0', '2')
    g.insert('0', '3')
    g.insert('1', '3')
    g.insert('2', '3')
    g.show_edge()

    gm = GraphMatrix(5)
    gm.insert(1,4)
    gm.insert(4,2)
    gm.insert(4,5)
    gm.insert(2,5)
    gm.insert(5,3)
    gm.show()
