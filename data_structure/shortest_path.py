"""
    Dijkstra 算法是一个贪婪算法，时间复杂度 O(VLogV)（使用最小堆）（不适用有负权值的边
    * 该算法适用广度优先搜索解决赋权有向图和无向图的单源最短路径问题，算法最终得到一个最短路径树

    Bellman-Ford 比 Dijkstra 算法更简单同事适用于分布式系统，复杂度 O(VE)，比Dijkstra算法慢（V为定点数，E 为边的个数）
"""


import heapq


def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = []
    while heap:
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


if __name__ == '__main__':
    G = {'0': [['1', 2], ['2', 5]],
         '1': [['0', 2], ['3', 3], ['4', 1]],
         '2': [['0', 5], ['5', 3]],
         '3': [['1', 3]],
         '4': [['1', 1], ['5', 3]],
         '5': [['2', 3], ['4', 3]]}
    shortDistance = dijkstra(G, '4', '2')
    print(shortDistance)

