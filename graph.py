class Edge(object):
    def __init__(self, value, weight=1, child=None):
        self.value = value
        self.weight = weight
        self.child = child


class Graph(object):
    def __init__(self, edges=None, directed=False):
        self.edges = edges if edges else []
        self.directed = directed
        # degree[] # keep list of degre of each vertex?
        # vertices? # num vertices
        # edges?    # num edges
        

def dfs(g):
    pass

def bfs():
    pass
