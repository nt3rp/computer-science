def dfs(g, start, path=None):
    """
    Assume that graph is of the form of an adjacency list:

    {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D', 'E'], 'D': ['C'], 'E': ['C'] }
    """
    if not path:
        path = []

    path.append(start)
    for v in g[start]:
        if not v in path:
            dfs(g, v, path)

    return path

def bfs(g, start):
    path = []
    q = [start]

    while q:
        v = q.pop(0)  # Equivalent to 'dequeue'

        if not v in path:
            path.append(v)
            q.extend(g[v])

    return path

def tbfs(g, start, proc=None):
    from collections import defaultdict

    if not proc:
        proc = {}

    state = defaultdict(unicode)
    path = [start]
    q = [start]
    state[start] = 'discovered'

    while q:
        v = q.pop(0)

        # process v

        for adj in g[v]:
            if not state[adj]:
                state[adj] = 'discovered'

                path.append(adj)
                q.append(adj)

        state[v] = 'processed'

    return path
