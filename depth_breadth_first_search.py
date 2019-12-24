
def dfs(G, s, S=None, res=None):
    """
        深度优先遍历
    """
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


if __name__ == '__main__':
    G = {'0': ['1', '2'],
         '1': ['2', '3'],
         '2': ['3', '5'],
         '3': ['4'],
         '4': [],
         '5': []}
    print(dfs(G, '0'))
    print(bfs(G, '0'))


