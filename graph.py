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

def bfs():
    pass
