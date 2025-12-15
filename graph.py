
class Graph:
    def __init__(self):
        self.adj = {}
        self.pos = {}

    def add_node(self, node, x, y):
        self.adj[node] = []
        self.pos[node] = (x, y)

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))  # undirected graph
